import sys
from pathlib import Path
path = Path.cwd().parent.parent
sys.path.append(str(path))

from config.postgres import Session
from database.models import User 
from .exceptions import UserNotFound



def get_user (username : str , session : Session) -> User:
    user  = session.query(User).filter(User.username == username).first()
    if not user:
        raise UserNotFound(username = username)
    else:
        return user
