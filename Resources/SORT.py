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
        names_informations_offset = br.read_int()
        br.seek(4, 1)
        
        br.seek(self.position + names_informations_offset, 0)
        print(br.tell())
        names_informations =  []
        for i in range(name_count):
            names_informations.append(br.read_ints(2))

        self.names = [-1 for _ in range(name_count)]
        for i, name_information in enumerate(names_informations):
            br.seek(self.position + names_offset + name_information[0], 0)
            
            # Get the size of the string with the offsets
            if i == len(names_informations) - 1:
                size = names_size - name_information[0]
            else:
                size = names_informations[i + 1][0] - name_information[0]
            
            # Separe the two strings from the zeros
            name_data = br.read_bytes(size)
            zero_indices = [i for i, byte in enumerate(name_data) if byte == 0]
            part1 = name_data[:zero_indices[0]]
            part2 = name_data[zero_indices[-1] + 1:]
                            
            # Attach the two strings and reverse it
            self.names[name_information[1]] = br.bytes_to_string((part2 + part1)[::-1])