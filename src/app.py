
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import requests

app = FastAPI()

@app.post("/")
async def root(params: Request):
    data = await params.json()

    data["is_success"] = True
    
    return JSONResponse(data)

#if __name__ == "__main__":
def run():
    uvicorn.run(app, host = "0.0.0.0", port = 8000)