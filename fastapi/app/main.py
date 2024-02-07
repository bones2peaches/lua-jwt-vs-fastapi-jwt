from database.healthcheck import check_postgres
from config.postgres import  db_dependency

from resources.user.schema import UserIn , UserOut , UserSession , CurrentUser
from resources.user.utils import get_current_user
from resources.user.exceptions import UserNotFound , DuplicateUsernameError , CredentialError

from fastapi.responses import JSONResponse
from fastapi.security import  OAuth2PasswordRequestForm
from typing_extensions import Annotated

from fastapi import FastAPI , Request , Depends

app = FastAPI()

@app.exception_handler(UserNotFound)
async def user_not_found_eh(request: Request, exc: UserNotFound):
    return JSONResponse(
        status_code= exc.status_code,
        content={"error" :{ "message": exc.message }},
    )


@app.exception_handler(DuplicateUsernameError)
async def duplicate_user_eh(request: Request, exc: DuplicateUsernameError):
    return JSONResponse(
        status_code= exc.status_code,
        content={"error" :{ "message": exc.message }},
    )


@app.exception_handler(CredentialError)
async def credentials_eh(request: Request, exc: CredentialError):
    return JSONResponse(
        status_code= exc.status_code,
        content={"error" :{ "message": exc.message }},
    )


@app.post('/user', response_model = UserOut)
async def create_user(db : db_dependency ,
                       payload : UserIn):
    new_user = payload.create(session = db)
    return new_user


@app.post('/session' , response_model = UserSession)
async def create_session (db : db_dependency, 
                          payload: Annotated[OAuth2PasswordRequestForm, Depends()] ,):
    
    payload = UserIn(username = payload.username , password = payload.password)
    session = payload.create_session(session= db)
    return session


@app.get('/protected')
async def protected(user : CurrentUser = Depends(get_current_user)  ):
    return str(user.user_id)

