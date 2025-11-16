from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI(title="Example API for AutoDoc")


class EchoInput(BaseModel):
    name: str
    age: int


@app.get("/hello")
def hello():
    """
    Returns a simple greeting message.
    Useful for testing basic GET requests and server health.
    """
    return {"msg": "Hello World"}


@app.get("/hello/{name}")
def hello_user(name: str):
    """
    Returns a personalized greeting message using path parameters.
    """
    return {"msg": f"Hello, {name}!"}


@app.post("/echo")
def echo(data: EchoInput = Body(..., description="JSON payload with name and age")):
    """
    Echoes back the JSON payload provided by the user.
    Validates input using a Pydantic model.
    """
    return {"received": data.dict()}
