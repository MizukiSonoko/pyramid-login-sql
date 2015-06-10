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
            user1 = User(name='user', passwd=hashlib.md5('password').hexdigest(), group='editor')
            user2 = User(name='admin', passwd=hashlib.md5('Password').hexdigest(), group='admin')
            page = Page(name='sample', data='This is sample', author='user')
            DBSession.add(user1)
            DBSession.add(user2)
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

    def test_signup_01(self):
        res = self.app.get('/signup',status=200)
        self.assertTrue( b'Signup' in res.body)
     
    def test_signup_02(self):
        res = self.app.post('/signup',{
            'form.submitted':'form.submitted',
            'name':'',
            'password':'',
            'repassword':','
        },status=200)
        self.assertTrue( b'Signup' in res.body)

    def test_signup_03(self):
        res = self.app.post('/signup',{
            'form.submitted':'form.submitted',
            'name':'hoge',
            'password':'pass',
            'repassword':'passwd',
        },status=200)
        self.assertTrue( b'Re-password' in res.body)

    def test_signup_04(self):
        res = self.app.post('/signup',{
            'form.submitted':'form.submitted',
            'name':'user',
            'password':'passwd',
            'repassword':'passwd',
        },status=200)
        self.assertTrue( b'There' in res.body)

    def test_signup_05(self):
        res = self.app.post('/signup',{
            'form.submitted':'form.submitted',
            'name':'',
            'password':'passwd',
            'repassword':'passwd',
        },status=200)
        self.assertTrue( b'Signup' in res.body)

    def test_signup_06(self):
        res = self.app.post('/signup',{
            'form.submitted':'form.submitted',
            'name':'user2',
            'password':'passwd',
            'repassword':'passwd',
        },status=302)

    def test_signup_07(self):
        res = self.app.post('/signup',{
            'form.submitted':'form.submitted',
            'name':'user2',
            'password':'passwd',
            'repassword':'passwd',
        },status=302)

        res = self.app.get('/',status=200)
        self.assertTrue( b'user2' in res.body)


    def test_admin_01(self):
        res = self.app.get('/admin',status=200)
        self.assertTrue( b'Login' in res.body)

    def test_admin_02(self):
        res = self.app.post('/login' , 
            {'form.submitted':'form.submitted',
             'login':'admin',
             'password':'Password'}, status=302)

        res = self.app.get('/admin', status=200)
        self.assertTrue( b'Admin' in res.body)
        self.assertTrue( b'user' in res.body)

    def test_admin_03(self):
        res = self.app.post('/login' , 
            {'form.submitted':'form.submitted',
             'login':'admin',
             'password':'Password'}, status=302)
         
        res = self.app.post('/admin',
            {'form.submitted':'form.submitted',
             'deluser':'user'}, status=302)

        res = self.app.post('/admin', status=200)
        self.assertTrue( not  b'<p>user</p>' in res.body)


