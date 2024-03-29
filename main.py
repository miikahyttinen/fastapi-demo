import uvicorn
from fastapi import FastAPI
import os

# load environment variables
# port = os.environ["PORT"]
port = 8000

# initialize FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"data": "Application ran successfully and deployed with GH action - FastAPI"}
  
  
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)