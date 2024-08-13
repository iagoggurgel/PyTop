from dataclasses import dataclass
from os import scandir, DirEntry
from json import dumps
from .config import ENV
from .defaults import Constants
from time import sleep

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
            pass
            sleep(5)
    
    def toJson(self) -> str:
        _ = list()
        for process in self.processList:
            _.append(process.toDict())
        return dumps(
            obj=_
        )

@dataclass()
class Process():
    """
    Class for storing Process Information.
    """
    pid: str = ''
    name: str = ''
    state: str = ''
    memSize: str = ''
    commandLine: str = ''
    threads: int = 0
    elapsed: float = 0

    def __init__(self, DIR: DirEntry) -> None:
        self.DIR: DirEntry = DIR
        self.setProcessInfo()

    def setProcessInfo(self) -> None:
        """
        Opens Status / Sched / Cmdline files and sets the Process Information.
        """
        def parseLine(line: str):
            return tuple(line.replace('\t', '').split(':'))

        with open(f'{self.DIR.path}/{Constants.STATUS}') as FILE:
            for line in FILE.readlines():
                parsedLine = parseLine(line)
                match parsedLine[Constants.KEY]:
                    case Constants.PID:
                        self.pid = parsedLine[Constants.VALUE]
                    case Constants.NAME:
                        self.name = parsedLine[Constants.VALUE]
                    case Constants.STATE:
                        self.state = parsedLine[Constants.VALUE]
                    case Constants.MEMSIZE:
                        self.memSize = parsedLine[Constants.VALUE]
                    case Constants.THREADS:
                        self.threads = int(parsedLine[Constants.VALUE])
                        break

        with open(f'{self.DIR.path}/{Constants.SCHED}') as FILE:
            for line in FILE.readlines():
                parsedLine = parseLine(line)
                if Constants.ELAPSED in parsedLine[Constants.KEY]:
                    self.elapsed = float(parsedLine[Constants.VALUE])


        with open(f'{self.DIR.path}/{Constants.CMDLINE}') as FILE:
            self.commandLine = FILE.read()

    @property
    def processIsEmpty(self) -> bool:
        return self.name == '' and self.state == '' and self.pid == '' and self.memSize == '' and self.commandLine == '' and self.threads == 0 and self.elapsed == 0
    
    def toDict(self) -> dict:
        return {
            "pid": self.pid,
            "name": self.name,
            "status": self.state,
            "memSize": self.memSize,
            "threads": self.threads,
            "elapsed": self.elapsed,
            "commandLine": self.commandLine,
        }

if __name__ == '__main__':
    sensor = ProcessSensor()
    print(sensor.toJson())