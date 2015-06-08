
from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    User,
)

GROUPS = {'editor':['group:editors']}

def groupfinder(userid, request):
    try:
        user = DBSession.query(User).filter(User.name == userid).first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    
    if user:
        return GROUPS.get(user.group, [])


