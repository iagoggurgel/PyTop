from dataclasses import dataclass
from json import dumps
from .config import ENV
from .defaults import Constants
from time import sleep
from io import TextIOWrapper

class CPUSensor():
    def __init__(self) -> None:
        self.CPU: CPU = None

    def scanCPU(self) -> None:
        while True:
            with open(f"{ENV.get('PROC_PATH')}{Constants.CPUINFO}") as FILE:
                updatedCPU: CPU = CPU(FILE)
            self.CPU = updatedCPU
            sleep(5)
    
    def toJson(self) -> str:
        return dumps(
            obj=self.CPU.toDict(),
            indent=4,
        )
    

class CPUCores():

    def __init__(self) -> None:
        self.clock: list = list()
        self.flags: list = list()
        self.cacheSize: list = list()
        self.TLBSize: list = list()

    def addClock(self, VALUE) -> None:
        self.clock.append(VALUE)
    
    def addFlags(self, VALUE) -> None:
        self.flags.append(VALUE)

    def addCacheSize(self, VALUE) -> None:
        self.cacheSize.append(VALUE)

    def addTLBSize(self, VALUE) -> None:
        self.TLBSize.append(VALUE)

    def toList(self) -> list[dict]: 
        _ = list()
        for x in range(len(self.clock)):
            _.append(dict(
                {
                    "clock" : self.clock[x],
                    "flags" : self.flags[x],
                    "cacheSize" : self.cacheSize[x],
                    "TLBSize" : self.TLBSize[x]
                }
            ))
        return _


@dataclass
class CPU():
    name: str = ''
    cores: CPUCores = None

    def __init__(self, FILE) -> None:
        self.FILE: TextIOWrapper = FILE
        self.setCPUInfo()

    def setCPUInfo(self) -> None:
        
        def parseLine(line: str):
            return tuple(line.replace('\t', '').split(':'))
        
        cpuCore = CPUCores()
        
        for line in self.FILE.readlines():
            parsedLine = parseLine(line)
            match parsedLine[Constants.KEY]:

                case Constants.MODELNAME:
                    self.name = parsedLine[Constants.VALUE]

                case Constants.CLOCK:
                    cpuCore.addClock(parsedLine[Constants.VALUE])

                case Constants.FLAGS:
                    cpuCore.addFlags(parsedLine[Constants.VALUE])

                case Constants.CACHESIZE:
                    cpuCore.addCacheSize(parsedLine[Constants.VALUE])

                case Constants.TLBSIZE:
                    cpuCore.addTLBSize(parsedLine[Constants.VALUE])

        self.cores = cpuCore


    def toDict(self) -> dict:

        cpuCore = self.cores.toList()
        
        return dict(
            {
                "name" : self.name,
                "numOfCores" : len(cpuCore),
                "coresInfo" : cpuCore
            }
        )



if __name__ == '__main__':
    cpuSensor = CPUSensor()
    cpuSensor.scanCPU()