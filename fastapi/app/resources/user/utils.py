from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import  Depends 
from typing_extensions import Annotated
from typing import Union
from jose import JWTError, jwt

from .schema import CurrentUser
from .exceptions import CredentialError
import uuid
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/session", auto_error=False) 


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)] ) -> CurrentUser :

    secret_key  ="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",
    algo = "HS256" 
    if not token:
        raise CredentialError()

    try:
        payload = jwt.decode(token, secret_key, algorithms=[algo])
        token_data = CurrentUser(user_id =  uuid.UUID(payload.get("user_id")),
        )
        return token_data
    except JWTError:
        raise CredentialError()
    


