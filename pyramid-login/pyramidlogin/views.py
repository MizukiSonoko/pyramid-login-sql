import re
from docutils.core import publish_parts

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )

from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    )

from .models import (
    DBSession,
    Page,
    User,
    )

from .security import ( 
    authenticate,
    )

@view_config(route_name='view_top', renderer='templates/top.mako')
def view_top(request):
    pages = DBSession.query(Page).all()
    if 'newpage' in request.params:
        return HTTPFound(location = request.route_url('add_page'))

    return dict(
        pages = pages
    )


@view_config(route_name='view_page', renderer='templates/view.mako')
def view_page(request):
    pagename = request.matchdict['pagename']
    page = DBSession.query(Page).filter_by(name=pagename).first()
    if page is None:
        return HTTPNotFound('No such page')

    edit_url = '/view/' + page.name + '/edit'

    return dict(
        page=page,
        edit_url=edit_url,
        logged_in=authenticated_userid(request))

@view_config(route_name='add_page', renderer='templates/add.mako',
             permission='edit')
def add_page(request):
    
    pagename = ''
    if 'form.submitted' in request.params:
        pagename = request.params['pagename']
        body = request.params['body']
        author = authenticated_userid(request)
        page = Page(pagename, body, author)
        DBSession.add(page)
        return HTTPFound(location = request.route_url('view_page',
            pagename=pagename))

    save_url = request.route_url('add_page', pagename=pagename)
    page = Page('', '', '')
    return dict(page=page, save_url=save_url,
                logged_in=authenticated_userid(request))

@view_config(route_name='edit_page', renderer='templates/edit.mako',
             permission='edit')
def edit_page(request):
    
    pagename = request.matchdict['pagename']
    page = DBSession.query(Page).filter_by(name=pagename).one()
    if 'form.submitted' in request.params:
        if page.author == authenticated_userid(request):
            page.data = request.params['body']
            DBSession.add(page)
            return HTTPFound(location = request.route_url('view_page',
                pagename=pagename))
    return dict(
        page=page,
        save_url = request.route_url('edit_page', pagename=pagename),
        logged_in=authenticated_userid(request),
        )

@view_config(route_name='login', renderer='templates/login.mako')
@forbidden_view_config(renderer='templates/login.mako')
def login(request):
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    message = ''
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        
        if authenticate(login, password):
            headers = remember(request, login)
            return HTTPFound(location = came_from,
                headers = headers)
        message = 'Failed login'

    return dict(
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = login,
        password = password,
        )

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('view_top'),
                     headers = headers)


