from mathutils import *

from ..Utilities import *

class BFMDLNODE:
    def __init__(self) -> None:
        self.scale = None
        self.translation = None
        self.rotation = None
        self.parent_index = -1
        self.child_index = -1
        self.next_sibling_index = -1
        self.previous_sibling_index = -1
        self.is_bone = 0

    def read(self, br):
        br.seek(16, 1)
        self.scale = Vector((br.read_floats(3)))
        br.seek(4, 1)
        self.translation = Vector((br.read_floats(3)))
        br.seek(4, 1)
        self.rotation = Euler((br.read_floats(3)), "XYZ")
        br.seek(4, 1)
        self.parent_index = br.read_short()
        self.child_index = br.read_short()
        self.next_sibling_index = br.read_short()
        self.previous_sibling_index = br.read_short()
        self.unk2 = br.read_short()
        self.is_bone = br.read_short()
        self.unk4 = br.read_short()
        self.unk5 = br.read_short()
        br.seek(64, 1)
        br.seek(64, 1)

    def compute_world_transform(self):

        return Matrix.Translation(self.translation) @ self.rotation.to_matrix().to_4x4() @ Matrix.Scale(1, 4, self.scale)
