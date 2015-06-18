# -*- coding: utf-8 -*-
import re

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
from .manager import (
    allUser,
    delUser,
    addUser,
    exist,
    )

from .domain_info import domain

@view_config(route_name='view_top', renderer='templates/top.mako')
def view_top(request):
    pages = DBSession.query(Page).all()
    user  = exist( authenticated_userid(request))
    if 'newpage' in request.params:
        return HTTPFound(location = domain + "/add_page") #request.route_url('add_page'))

    return dict(
        domain = domain,
        pages = pages,
        user = user
    )


@view_config(route_name='view_page', renderer='templates/view.mako')
def view_page(request):
    pagename = request.matchdict['pagename']
    page = DBSession.query(Page).filter_by(name=pagename).first()
    if page is None:
        return HTTPNotFound('No such page.')

    edit_url = '/view/' + page.name + '/edit'

    return dict(
        domain = domain,
        page=page,
        edit_url=edit_url,
        logged_in=authenticated_userid(request)
    )

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
        return HTTPFound(location = domain +"/view/"+pagename)

    save_url = domain + '/add_page'# , pagename=pagename)
    page = Page('', '', '')
    return dict(page=page, save_url=save_url,
                logged_in=authenticated_userid(request),
                domain = domain,
    )

@view_config(route_name='edit_page', renderer='templates/edit.mako',
             permission='edit')
def edit_page(request):
    
    pagename = request.matchdict['pagename']
    page = DBSession.query(Page).filter_by(name=pagename).one()
    if 'form.submitted' in request.params:
        if page.author == authenticated_userid(request):
            page.data = request.params['body']
            DBSession.add(page)
            return HTTPFound(location = domain + "/view/"+ pagename)
    return dict(
        domain = domain,
        page=page,
        save_url = domain + "/view/" + pagename +"/edit" ,#request.route_url('edit_page', pagename=pagename),
        logged_in=authenticated_userid(request),
    )

@view_config(route_name='signup', renderer='templates/signup.mako')
def signup(request):
    name = ''
    password = ''
    if 'form.submitted' in request.params:
        name = request.params['name']
        password = request.params['password']
        repassword = request.params['repassword']        
        if not name or not password or not repassword:
            return dict(
                name=name,
                )

        if password != repassword:
            return dict(
                name=name,
                message='Re-password is different from password!'
            )
        if exist(name):
            return dict(
                name=name,
                message='There is already a user named '+name+'.!'
            )

        if addUser(name, password):
            headers = remember(request, name)
            return HTTPFound(location = domain + "/", #request.route_url('view_top'),
                headers = headers)
        else:
            return dict(
                name=name,
                message='DB Error!'
            )

    return dict(
        name=name,
        message=None
    )


@view_config(route_name='admin', renderer='templates/admin.mako', permission='admin')
def admin_page(request):
    users = allUser()
    message = ''
   
    #if users:
    #    users = []
    #    message = 'DB error!'

    if 'deluser' in request.params:
            user = request.params['deluser']
            if delUser(user):
                return HTTPFound(location = domain + "/admin" ) #request.route_url('admin'))
            else:
                message = "Deleting user failed." 
    return dict(
        message=message,
        users=users,
        logged_in=authenticated_userid(request),
    )



@view_config(route_name='login', renderer='templates/login.mako')
@forbidden_view_config(renderer='templates/login.mako')
def login(request):
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = domain+ referrer
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
        url =  domain + '/login', #request.application_url + '/login',
        came_from = came_from,
        login = login,
        password = password,
    )

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = domain + "/", #request.route_url('view_top'),
                     headers = headers)


