from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return "Working"

@app.get("/puesto/{id}",response_class=FileResponse)
def getQR(id:int):
    return FileResponse("./index.html")