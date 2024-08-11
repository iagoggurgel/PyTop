from dataclasses import dataclass
from json import dumps
from .config import ENV
from .defaults import Constants
from time import sleep
from io import TextIOWrapper

class DiskSensor():
    
    def __init__(self) -> None:
        self.disk: Disk = None
    
    def scanRAM(self) -> None:
        while True:
            with open(f"{ENV.get('PROC_PATH')}{Constants.MEMFILE}") as FILE:
                updatedDisk: Disk = Disk(FILE)
            self.disk = updatedDisk
            sleep(5)
    
    def toJson(self) -> str:
        return dumps(
            obj=self.disk.toDict(),
            indent=4,
        )

@dataclass()
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