"""
    Modelo de armazenamento de dados da RAM.
"""


from io import TextIOWrapper
from src.defaults import Constants

class RAM():

    def __init__(self, FILE) -> None:
        self.FILE: TextIOWrapper = FILE
        self.setRAMInfo()

    def setRAMInfo(self) -> None:
        
        def parseLine(line: str):
            return tuple(line.replace('\t', '').split(':'))
        
        for line in self.FILE.readlines():
            parsedLine = parseLine(line)
            match parsedLine[Constants.KEY]:

                case Constants.MEMTOTAL:
                    self.memTotal = parsedLine[Constants.VALUE].strip('\n')
                
                case Constants.MEMFREE:
                    self.memFree = parsedLine[Constants.VALUE].strip('\n')

                case Constants.MEMAVAILABLE:
                    self.memAvailable = parsedLine[Constants.VALUE].strip('\n')

                case Constants.MEMCACHED:
                    self.memCached = parsedLine[Constants.VALUE].strip('\n')
                
                case Constants.SWAPTOTAL:
                    self.swapTotal = parsedLine[Constants.VALUE].strip('\n')

                case Constants.SWAPFREE:
                    self.swapFree = parsedLine[Constants.VALUE].strip('\n')

                

    def toDict(self) -> dict:
        return dict(
            {
                "memTotal" : self.memTotal,
                "memFree" : self.memFree,
                "memAvailable" : self.memAvailable,
                "memCached" : self.memCached,
                "swapTotal" : self.swapTotal,
                "swapFree" : self.swapFree,
            }
        )