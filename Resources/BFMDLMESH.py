from ..Utilities import *

class BFMDLMESH:
    def __init__(self) -> None:
        self.start_index = 0
        self.submeshs_count = 0
        self.name_index = -1

    def read(self, br):
        br.seek(16, 1)
        self.unk1 = br.read_short()
        self.unk2 = br.read_short()
        self.start_index = br.read_short()
        self.submeshs_count = br.read_short()
        self.unk3 = br.read_short()
        self.unk4 = br.read_short()
        self.unk5 = br.read_short()
        self.name_index = br.read_short()
        br.seek(28, 1)
        self.unk6 = br.read_int()