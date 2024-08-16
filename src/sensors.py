"""
    Módulo de desenvolvimento dos sensores dos processos / CPU / RAM.
"""


from os import scandir
from json import dumps
from .config import ENV
from time import sleep
from .models import Process
from .models import CPU
from .models import RAM
from .models import Disk
from .defaults import Constants

class ProcessSensor():

    def __init__(self) -> None:
        self.processList: list[Process] = None

    def scanProcesses(self) -> None:
        try:
            while True:
                processList: list[Process] = list()
                with scandir(ENV.get('PROC_PATH')) as procDir:
                    for process in procDir:
                        if process.is_dir() and process.name.isnumeric():
                            newProcess = Process(
                                DIR=process
                            )
                            if newProcess.processIsEmpty:
                                continue
                            processList.append(newProcess)
                self.processList = processList
        except:
            sleep(5)
            pass
            
    
    def toList(self) -> str:
        _ = list()
        for process in self.processList:
            _.append(process.toDict())
        return _
    
class RAMSensor():

    def __init__(self) -> None:
        self.RAM: RAM = None
    
    def scanRAM(self) -> None:
        while True:
            with open(f"{ENV.get('PROC_PATH')}{Constants.MEMFILE}") as FILE:
                updatedRAM: RAM = RAM(FILE)
            self.RAM = updatedRAM
            sleep(5)
    
    def toDict(self) -> str:
        return self.RAM.toDict()

class CPUSensor():
    def __init__(self) -> None:
        self.CPU: CPU = None

    def scanCPU(self) -> None:
        while True:
            with open(f"{ENV.get('PROC_PATH')}{Constants.CPUINFO}") as FILE:
                updatedCPU: CPU = CPU(FILE)
            self.CPU = updatedCPU
            sleep(5)
    
    def toDict(self) -> str:
        return self.CPU.toDict()
    
class DiskSensor():
    pass
    
class NetworkSensor():
    pass