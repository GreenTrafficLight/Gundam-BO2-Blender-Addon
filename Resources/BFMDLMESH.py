class BFMDLMESH:
    def __init__(self) -> None:
        self.start_index = 0
        self.submeshs_count = 0
        self.end_index = 0

    def read(self, br):
        br.seek(16, 1)
        br.read_short()
        br.read_short()
        self.start_index = br.read_short()
        self.submeshs_count = br.read_short()
        self.end_index = br.read_short()
        br.read_short()
        br.read_short()
        br.read_short()
        br.seek(28, 1)
        br.seek(4, 1)