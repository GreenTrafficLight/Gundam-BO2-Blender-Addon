from ..Utilities import *

from .VTX import *

import os

class BFMDLSUBMESH:
    def __init__(self) -> None:
        self.face_count = 0
        self.vertex_count = 0
        self.stride = 0
        self.vtx_face_buffer_offset = 0
        self.vtx_vertex_buffer_offset = 0
        self.vtx = None

    def read(self, br):
        br.seek(16, 1)
        br.seek(16, 1)
        br.seek(24, 1)
        self.face_count = br.read_short()
        self.vertex_count = br.read_short()
        self.stride = br.read_byte()
        self.unk1 = br.read_byte()
        self.unk2 = br.read_short()
        self.vtx_face_buffer_offset = br.read_int()
        self.vtx_vertex_buffer_offset = br.read_int()
        self.unk3 = br.read_short()
        self.unk4 = br.read_short()
        self.unk5 = br.read_short()
        self.unk6 = br.read_short()
        br.seek(64, 1)

    def read_vtx(self, filepath):
        filename = os.path.basename(filepath)
        vtx_file = open(os.path.dirname(filepath) + "\\" +  filename.replace("_Mdl","_Vtx"), "br")
        vtx_br = BinaryReader(vtx_file)
        self.vtx = VTX()
        self.vtx.read(vtx_br, self)