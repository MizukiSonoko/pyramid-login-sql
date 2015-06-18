# -*- coding: utf-8 -*-

import hashlib

from sqlalchemy.exc import DBAPIError
from .models import (
    DBSession,
    User,
)

def allUser():
    try:
        users = DBSession.query(User).all()
    except DBAPIError:
        return None

    return users

def delUser(name):
    try:
        user = DBSession.query(User).filter(User.name == name).one()
        DBSession.delete(user)
    except DBAPIError:
        return False

    return True

def addUser(name, password):
    try:
        user = User(name=name, passwd=hashlib.md5(password).hexdigest(), group='editor')        
        DBSession.add(user)
    except DBAPIError:
        return False

    return True

def exist(name):
    try:
        user = DBSession.query(User).filter(User.name == name).first()
    except DBAPIError:
        return False

    if not user:
        return False
    return user

