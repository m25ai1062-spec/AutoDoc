from fastapi import FastAPI

app = FastAPI(title="Example API for AutoDoc")

@app.get("/hello")
def hello():
    """Returns a greeting message."""
    return {"msg": "Hello World"}

@app.post("/echo")
def echo(data: dict):
    """Returns whatever data you send (simple echo)."""
    return {"received": data}
