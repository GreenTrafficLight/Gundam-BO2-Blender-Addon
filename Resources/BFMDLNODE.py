from ..Utilities import *

class BFMDLNODE:
    def __init__(self) -> None:
        self.parent_ID = -1

    def read(self, br):
        br.seek(16, 1)
        br.seek(48, 1)
        self.parent_ID = br.read_short()
        br.read_short()
        br.read_short()
        br.read_short()
        br.read_short()
        br.read_short()
        br.read_short()
        br.read_short()
        br.seek(64, 1)
        br.seek(64, 1)