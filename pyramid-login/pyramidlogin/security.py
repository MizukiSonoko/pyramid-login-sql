# -*- coding: utf-8 -*-

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    User,
)
import hashlib

GROUPS = {
    'editor':['group:editors'],
    'admin':['group:admins'],
}


def authenticate(name, password):   
    try:
        user = DBSession.query(User).filter(User.name == name).first()
    except DBAPIError:
        return False

    if not user:
        return False
    

    if user.passwd == hashlib.md5(password).hexdigest():
        return True
    return False

def groupfinder(name, request):
    try:
        user = DBSession.query(User).filter(User.name == name).one()
    except DBAPIError:
        return []   
 
    if user:
        return GROUPS.get(user.group, [])


