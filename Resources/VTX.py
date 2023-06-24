from ..Utilities import *

class VTX:
    def __init__(self) -> None:
        self.positions = []
        self.normals = []
        self.uvs = []
        self.bone_indices = []
        self.bone_weights = []
        self.face_indices = []

    def read(self, br, bfmdl_submesh):

        position = 0

        br.seek(bfmdl_submesh.vtx_vertex_buffer_offset, 0)

        if bfmdl_submesh.stride == 24:
            
            for i in range(bfmdl_submesh.vertex_count):
                #br.seek(bfmdl_submesh.vtx_vertex_buffer_offset + bfmdl_submesh.stride * i + position, 0)
                self.positions.append(Vector((br.read_floats(3))))
                br.seek(12, 1)
        
        elif bfmdl_submesh.stride == 28:
            
            for i in range(bfmdl_submesh.vertex_count):
                self.positions.append(Vector((br.read_floats(3))))
                br.seek(16, 1)

        elif bfmdl_submesh.stride == 32:
            
            for i in range(bfmdl_submesh.vertex_count):
                self.positions.append(Vector((br.read_floats(3))))
                self.bone_indices.append(br.read_ubyte())
                br.read_ubytes(3)
                br.seek(4, 1)
                self.uvs.append(Vector((br.read_half_floats(2))))
                br.seek(8, 1)

        else :
             print(bfmdl_submesh.stride)


        br.seek(bfmdl_submesh.vtx_face_buffer_offset, 0)

        for i in range(bfmdl_submesh.face_count):
                self.face_indices.append(br.read_ushorts(3))