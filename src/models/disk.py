"""
    Modelo de armazenamento de dados do disco.
"""

from io import TextIOWrapper
from src.defaults import Constants

class Disk():
    
    def __init__(self, FILE) -> None:
        self.FILE: TextIOWrapper = FILE
        self.setDiskInfo()

    def setDiskInfo(self) -> None:
        
        def parseLine(line: str):
            return tuple(line.replace('\t', '').split(':'))
        
        for line in self.FILE.readlines():
            parsedLine = parseLine(line)
            match parsedLine[Constants.KEY]:

                case Constants.MEMTOTAL:
                    self.memTotal = parsedLine[Constants.VALUE]
                
                case Constants.MEMFREE:
                    self.memFree = parsedLine[Constants.VALUE]

                case Constants.MEMAVAILABLE:
                    self.memAvailable = parsedLine[Constants.VALUE]

                case Constants.MEMCACHED:
                    self.memCached = parsedLine[Constants.VALUE]
                
                case Constants.SWAPTOTAL:
                    self.swapTotal = parsedLine[Constants.VALUE]

                case Constants.SWAPFREE:
                    self.swapFree = parsedLine[Constants.VALUE]

                

    def toDict(self) -> dict:
        pass