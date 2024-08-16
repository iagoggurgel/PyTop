"""
    Módulo raiz do projeto que deve ser executado usando o comando: fastapi dev app.py

    Inicia as rotas da API e as Threads de gerência de estados.
"""


from fastapi import FastAPI
from .config import ENV
from .sensors import *
from threading import Thread
import os, signal


app = FastAPI(
    title="PyTop",
    description="An API for retrieval of Linux Hardware Usage Data",
    version="BETA"
)

processSensor = ProcessSensor()
cpuSensor = CPUSensor()
ramSensor = RAMSensor()

processThread = Thread(
    target=processSensor.scanProcesses,
    daemon = True
)

cpuThread = Thread(
    target=cpuSensor.scanCPU,
    daemon = True
)

ramThread = Thread(
    target=ramSensor.scanRAM,
    daemon = True
)

processThread.start()
cpuThread.start()
ramThread.start()

@app.get("/process/")
def getProcesses():
    return processSensor.toList()

@app.get("/cpu/")
def getCPUInfo():
    return cpuSensor.toDict()

@app.get("/memory/")
def getRAMUsage():
    return ramSensor.toDict()

@app.post("/signal/kill/{pid}")
def killProcess(pid: int):
    try:
        os.kill(pid, signal.SIGKILL)
        return {"message": f"Process {pid} killed successfully!"}
    except:
        return {"message": f"Process {pid} was not killed successfully!"}
    

@app.post("/signal/pause/{pid}")
def pauseProcess(pid: int):
    try:
        os.kill(pid, signal.SIGSTOP)
        return {"message": f"Process {pid} stopped successfully!"}
    except:
        return {"message": f"Process {pid} was not stopped successfully!"}

@app.post("/signal/continue/{pid}")
def continueProcess(pid: int):
    try:
        os.kill(pid, signal.SIGSTOP)
        return {"message": f"Process {pid} continued successfully!"}
    except:
        return {"message": f"Process {pid} was not continued successfully!"}
