from pydantic import BaseModel, Field 
from typing import List, Optional 
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError



import sys
from pathlib import Path
path = Path.cwd().parent.parent
sys.path.append(str(path))

from config.postgres import Session
from database.models import User 
from resources.user.exceptions import DuplicateUsernameError , CredentialError
from .crud import get_user 

import uuid
from datetime import datetime , timedelta
from jose import JWTError, jwt


class CurrentUser (BaseModel):
    user_id : uuid.UUID  = Field(...)

class UserOut(BaseModel):
    message :str = 'user has been created successfully!'    


class UserSession(BaseModel):
    access_token : str
    type : str
    expires : datetime

class UserIn(BaseModel):
    username : str = Field(...)
    password : str = Field(...)

    def create(self  ,
                session : Session ) -> UserOut:

            
        
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 
        hashed_password = pwd_context.hash(self.password)

        user = User(username = self.username , hashed_password = hashed_password)
        try : 
            session.add(user)
            session.commit()
            return UserOut()
        except IntegrityError:
            # if name is duplicate 
            session.rollback()
            raise DuplicateUsernameError(username  = self.username , status_code=404)
        

    def create_session (self ,
                         session : Session , 
                          secret_key : str ="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",
                            algo :str= "HS256",
                             expires : int = 3600) -> str:
        

        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")      
        user = get_user(session= session , username = self.username)   
        password_check = pwd_context.verify(self.password , user.hashed_password)
        if not password_check:
            raise CredentialError     
        
        else:
            token_data = { 'user_id' :str(user.id) }
            expire = datetime.now() + timedelta(minutes = expires)
            token_data.update({"exp": expire})
            encoded_jwt = jwt.encode(token_data, secret_key, algorithm=algo)
            return UserSession(access_token = encoded_jwt , type = "bearer" , expires = expire)               

        










