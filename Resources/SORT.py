from ..Utilities import *

class SORT:
    def __init__(self) -> None:
        self.position = 0
        self.names = []

    def read(self, br):
        self.position = br.tell()
        br.seek(4, 1)
        name_count = br.read_int()
        names_size = br.read_int()
        br.seek(20, 1)
        names_offset = br.read_int()
        br.seek(4, 1)
        unknown_offset = br.read_int()
        br.seek(4, 1)
        
        br.seek(self.position + names_offset, 0)
        print(br.tell())
        for i in range(name_count):
            self.names.append(br.bytes_to_string(br.read_bytes(16)))

        # br.seek(self.position + unknown_offset, 1)
        # for i in range(name_count):
        #     br.seek(8, 1)