from fastapi import FastAPI
from .process import ProcessSensor
from .config import ENV

app = FastAPI(
    title="PyTop",
    description="An API for retrieval of Linux Hardware Usage Data",
    version="BETA"
)

@app.get("/process/")
def getProcesses():
    return ProcessSensor().toJson()

@app.get("/cpu/")
def getCpuUsage():
    return "<p>Hello, World!<p>"

@app.get("/disk/")
def getDiskUsage():
    return "<p>Hello, World!<p>"

@app.get("/memory/")
def getMemoryUsage():
    return "<p>Hello, World!<p>"

@app.get("/network/")
def getNetworkUsage():
    return "<p>Hello, World!<p>"

@app.post("/kill/")
def killProcess(pid: int):
    return {"process" : pid}