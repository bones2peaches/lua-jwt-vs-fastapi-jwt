
from fastapi import FastAPI , Header

app = FastAPI()

from typing_extensions import Annotated

from typing import  Union





@app.get('/protected')
async def protected(x_user_id : Annotated[Union[str , None], Header()] = None  ):
    return str(x_user_id)

