from BFMDLNODE import *
from BFMDLMESH import *
from BFMDLSUBMESH import *

class BFMDLH:

    def __init__(self) -> None:
        self.bfmdlnodes = []
        self.bfmdlmeshs = []
        self.bfmdlsubmeshs = []

        self.bfmdlnodes_offset = 0
        self.bfmdlmeshs_offset = 0
        self.bfmdlsubmeshs_offset = 0

        self.bfmdlnodes_count = 0
        self.bfmdlmeshs_count = 0
        self.bfmdlsubmeshs_count = 0


    def read(self, br):
        br.seek(24, 1)
        unknown_offset1 = br.read_int()
        vtx_size = br.read_int()
        br.seek(16, 1)
        self.bfmdlnodes_offset = br.read_long()
        self.bfmdlmeshs_offset = br.read_long()
        self.bfmdlsubmeshs_offset = br.read_long()
        br.read_long()
        br.read_long()
        br.read_long()
        br.read_long()
        br.read_long()
        br.read_long()
        br.read_long()
        br.read_long() # bone indices ?
        br.read_long()
        self.sort1_offset = br.read_long()
        self.sort2_offset = br.read_long()
        self.bfmdlnodes_count = br.read_int()
        self.bfmdlmeshs_count = br.read_int()
        self.bfmdlsubmeshs_count = br.read_int()

        self.read_bfmdlnodes(br)
        self.read_bfmdlmeshs(br)
        self.read_bfmdlsubmeshs(br)

    def read_bfmdlnodes(self, br):
        br.seek(self.bfmdlnodes_offset, 0)
        for i in range(self.bfmdlnodes_count):
            bfmdlnode = BFMDLNODE()
            bfmdlnode.read(br)
            self.bfmdlnodes.append(bfmdlnode)

    def read_bfmdlmeshs(self, br):
        br.seek(self.bfmdlmeshs_offset, 0)
        for i in range(self.bfmdlmeshs_count):
            bfmdlmesh = BFMDLMESH()
            bfmdlmesh.read(br)
            self.bfmdlnodes.append(bfmdlmesh)

    def read_bfmdlsubmeshs(self, br):
        br.seek(self.bfmdlsubmeshs_offset, 0)
        for i in range(self.bfmdlsubmeshs_count):
            bfmdlsubmesh = BFMDLSUBMESH()
            bfmdlsubmesh.read(br)
            self.bfmdlsubmeshs.append(bfmdlsubmesh)


