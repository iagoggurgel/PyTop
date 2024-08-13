from fastapi import FastAPI
from .process import ProcessSensor
from .cpu import CPUSensor
from .config import ENV
from .memory import RAMSensor
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
    target=processSensor.scanProcesses
)

cpuThread = Thread(
    target=cpuSensor.scanCPU
)

ramThread = Thread(
    target=ramSensor.scanRAM
)

processThread.start()
cpuThread.start()
ramThread.start()

@app.get("/process/")
def getProcesses():
    return processSensor.toJson()

@app.get("/cpu/")
def getCPUInfo():
    return cpuSensor.toJson()

@app.get("/memory/")
def getRAMUsage():
    return ramSensor.toJson()

@app.post("/signal/kill")
def killProcess(pid: int):
    os.kill(pid, signal.SIGKILL)
    return {"message": f"Process {pid} killed successfully!"}

@app.post("/signal/pause")
def pauseProcess(pid: int):
    os.kill(pid, signal.SIGSTOP)
    return {"message": f"Process {pid} paused successfully!"}

@app.post("/signal/continue")
def continueProcess(pid: int):
    os.kill(pid, signal.SIGCONT)
    return {"message": f"Process {pid} continued successfully!"}