import unittest
import transaction
import hashlib

from pyramid import testing

from .models import DBSession


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            User,
            Page,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            user = User(name='user', passwd=hashlib.md5('password').hexdigest(), group='editor')
            page = Page(name='sample', data='This is sample', author='user')
            DBSession.add(user)
            DBSession.add(page)
    
        from pyramidlogin import main   
        from webtest import TestApp
        a = main({}, **{'sqlalchemy.url': 'sqlite://'})
        self.app = TestApp(a)

    def tearDown(self):
        del self.app
        DBSession.remove()
        testing.tearDown()

    def test_top_page(self):
        res = self.app.get('/', status=200)
        self.assertTrue( b'Top Page' in res.body)
        self.assertTrue( b'sample' in res.body)

    def test_access_add_page_01(self):
        res = self.app.get('/', {'newpage':'newpage'}, status=302)
        self.assertEqual(res.location, 'http://localhost/add_page')
    
        res = self.app.get('/add_page', status=200)
        self.assertTrue( b'Login' in res.body)


    def test_login(self):
        res = self.app.get('/add_page', status=200)
        self.assertTrue( b'Login' in res.body)

    def test_login(self):
        res = self.app.get('/login', status=200)
        self.assertTrue( b'Login' in res.body)
 
    def test_login_failed_01(self):
        res = self.app.post('/login' , 
            {'form.submitted':'form.submitted',
             'login':'wrongUser',
             'password':'wrongPassword'}, status=200)
        self.assertTrue( b'Login' in res.body)

    def test_login_failed_02(self):
        res = self.app.post('/login' , 
            {'form.submitted':'form.submitted',
             'login':'wrongUser',
             'password':'password'}, status=200)
        self.assertTrue( b'Login' in res.body)

    def test_login_failed_03(self):
        res = self.app.post('/login' , 
            {'form.submitted':'form.submitted',
             'login':'user',
             'password':'wrongPassword'}, status=200)
        self.assertTrue( b'Login' in res.body)

    def test_login_success(self):
        res = self.app.post('/login' , 
            {'form.submitted':'form.submitted',
             'login':'user',
             'password':'password'}, status=302)
        self.assertEqual(res.location, 'http://localhost/')

    def test_access_add_page_02(self):
        res = self.app.post('/login' , 
            {'form.submitted':'form.submitted',
             'login':'user',
             'password':'password'}, status=302)

        res = self.app.get('/add_page', status=200)
        self.assertTrue( b'TopPage' in res.body)

    def test_add_page_01(self):
        res = self.app.post('/login' , 
            {'form.submitted':'form.submitted',
             'login':'user',
             'password':'password'}, status=302)

        res = self.app.post('/add_page', 
            {'form.submitted':'form.submitted',
             'pagename':'pagename',
             'body':'Body'},status=302)

        self.assertEqual(res.location, 'http://localhost/view/pagename')

        res = self.app.get('/', status=200)
        self.assertTrue( b'Top Page' in res.body)
        self.assertTrue( b'pagename' in res.body)



