"""
    Módulo que mantêm as informações estáticas de Parsing.
"""


from pathlib import Path

class Constants():
    ENVPATH = Path(__file__).parent.parent / '.env'


    # PROCESS FILES
    STATUS = 'status'
    SCHED = 'sched'
    CMDLINE = 'cmdline'

    # PROCESS ATTRIBUTES
    NAME = 'Name'
    STATE = 'State'
    PID = 'Pid'
    MEMSIZE = 'VmSize'
    THREADS = 'Threads'
    ELAPSED = 'se.sum_exec_runtime'

    # CPU FILE
    CPUINFO = 'cpuinfo'

    # CPU ATTRIBUTES
    MODELNAME = 'model name'
    CLOCK = 'cpu MHz'
    CACHESIZE = 'cache size'
    FLAGS = 'flags'
    TLBSIZE = 'TLB size'

    # MEM FILE
    MEMFILE = 'meminfo'

    # MEM ATTRIBUTES
    MEMTOTAL = 'MemTotal'
    MEMFREE = 'MemFree'
    MEMAVAILABLE = 'MemAvailable'
    MEMCACHED = 'Cached'
    SWAPTOTAL = 'SwapTotal'
    SWAPFREE = 'SwapFree'

    KEY = 0
    VALUE = 1


class ENVNotFound(Exception):
    pass