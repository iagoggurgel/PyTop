from pathlib import Path

class Constants():
    ENVPATH = Path(__file__).parent.parent / '.env'


class ENVNotFound(Exception):
    pass