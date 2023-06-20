class BFMDLSUBMESH:
    def __init__(self) -> None:
        self.face_count = 0
        self.vertex_count = 0
        self.stride = 0
        self.vtx_face_buffer_offset = 0
        self.vtx_vertex_buffer_offset = 0

    def read(self, br):
        br.seek(16, 1)
        br.seek(16, 1)
        br.seek(24, 1)
        self.face_count = br.read_short()
        self.vertex_count = br.read_short()
        self.stride = br.read_byte()
        br.read_byte()
        br.read_short()
        self.vtx_face_buffer_offset = br.read_int()
        self.vtx_vertex_buffer_offset = br.read_int()
        br.read_short()
        br.read_short()
        br.read_short()
        br.read_short()
        br.seek(64, 1)