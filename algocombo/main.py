from typing import Union

from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def health_check():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Hello World"})

