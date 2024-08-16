"""
    Modelo de armazenamento de dados dos processos.
"""


from os import DirEntry
from src.defaults import Constants

class Process():

    def __init__(self, DIR: DirEntry) -> None:
        self.DIR: DirEntry = DIR
        self.name: str = ''
        self.state: str = ''
        self.pid: str = ''
        self.memSize: str = ''
        self.commandLine: str = ''
        self.threads: int = 0
        self.elapsed: int = 0
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
                        self.pid = parsedLine[Constants.VALUE].strip('\n')
                    case Constants.NAME:
                        self.name = parsedLine[Constants.VALUE].strip('\n')
                    case Constants.STATE:
                        self.state = parsedLine[Constants.VALUE].strip('\n')
                    case Constants.MEMSIZE:
                        self.memSize = parsedLine[Constants.VALUE].strip('\n')
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