from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse

app = FastAPI(title="Hello Name API", version="1.0")

@app.get("/hello/{name}")
def say_hello(
    name: str = Path(..., min_length=1, max_length=50, description="Name to greet")
):
    """
    Returns a greeting message for the given name.
    """
    safe_name = name.strip()
    if not safe_name.isalpha():
        return JSONResponse(
            status_code=400,
            content={"error": "Name must contain only alphabetic characters."}
        )
    return {"message": f"Hello, {safe_name}!"}
