"""
    Modelo de armazenamento de dados da CPU.
"""


from src.defaults import Constants
from io import TextIOWrapper

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


class CPU():

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
                    self.name = parsedLine[Constants.VALUE].strip('\n')

                case Constants.CLOCK:
                    cpuCore.addClock(parsedLine[Constants.VALUE].strip('\n'))

                case Constants.FLAGS:
                    cpuCore.addFlags(parsedLine[Constants.VALUE].strip('\n'))

                case Constants.CACHESIZE:
                    cpuCore.addCacheSize(parsedLine[Constants.VALUE].strip('\n'))

                case Constants.TLBSIZE:
                    cpuCore.addTLBSize(parsedLine[Constants.VALUE].strip('\n'))

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

