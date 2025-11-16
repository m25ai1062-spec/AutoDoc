from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI(title="APIs for AutoDoc")


# -------------------------------
# Models
# -------------------------------
class EchoInput(BaseModel):
    name: str
    age: int


# -------------------------------
# Endpoints
# -------------------------------

@app.get("/hello")
def hello():
    """
    Returns a simple static greeting message.
    """
    return {"msg": "Hello World"}


@app.get("/hello/{name}")
def hello_user(name: str):
    """
    Returns a personalized greeting message for the given user.
    Demonstrates path parameter extraction.
    """
    return {"msg": f"Hello, {name}!"}


@app.post("/echo")
def echo(data: EchoInput = Body(..., description="Valid JSON payload containing name and age")):
    """
    Reverts back the JSON payload provided by the user.
    """
    return {"received": data.dict()}
