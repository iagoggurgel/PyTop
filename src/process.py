from dataclasses import dataclass
from os import scandir
from json import dumps
from .config import ENV

class ProcessSensor():
    
    def __init__(self) -> None:
        self.processes: list[Process] = self.getAllProcesses()

    def getAllProcesses(self):
        processList: list[Process] = list()
        with scandir(ENV.get('PROC_PATH')) as procDir:
            for process in procDir:
                thisProcess = Process()
                if process.is_dir() and process.name.isnumeric():
                    with open(f'{process.path}/status') as statusFile:
                        for line in statusFile.readlines():
                            splitted = line.split("\t")
                            match splitted[0]:
                                case 'Name:':
                                    thisProcess.name = splitted[1]
                                case 'State:':
                                    thisProcess.status = splitted[1]
                                case 'Pid:':
                                    thisProcess.pid = splitted[1]
                                case 'VmSize:':
                                    thisProcess.memSize = splitted[1]
                                case 'Threads:':
                                    thisProcess.threads = int(splitted[1])
                if thisProcess.processIsEmpty:
                    continue
                processList.append(thisProcess)
        
        return processList

    def toJson(self):
        _ = list()
        for process in self.processes:
            _.append(process.toDict())
        return dumps(_, indent=4)

@dataclass(init=False)
class Process():
    """
    Classe que armazena as informações pertinentes de um processo.
    """
    name: str = ''
    status: str = ''
    pid: str = ''
    memSize: str = ''
    threads: int = 0
    elapsed: int = 0

    @property
    def processIsEmpty(self):
        return self.name == '' and self.status == '' and self.pid == '' and self.memSize == '' and self.threads == 0 and self.elapsed == 0
    
    def toDict(self):
        return {
            "name": self.name,
            "status": self.status,
            "pid": self.pid,
            "memSize": self.memSize,
            "threads": self.threads,
            "elapsed": self.elapsed
        }

if __name__ == '__main__':
    processSensor = ProcessSensor()
    processSensor.toJson()
