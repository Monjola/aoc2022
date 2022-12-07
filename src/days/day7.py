from fileparse import file_rows_to_list
    
class File:
    size: int
    name: str
    def __init__(self,input:str):
        sizestr, self.name = input.split(' ')
        self.size = int(sizestr)


class Directory:
    subdirectories = {}
    files = []
    parent = None

    def add_subdirectory(self, line: str):
        discard, directory_name = line.split(' ')
        self.subdirectories[directory_name] = Directory()
        
    def add_file(self,file: File):
        self.files.append(file)
    

def cd(current_path:Directory, input:str) -> Directory:
    input, discard = input.split(' ')
    if input == '..':
        current_path = current_path.parent
    else:
        current_path = current_path.subdirectories[input]


def parseline(current_path:Directory, line:str):
    if "$ cd" in line:
        cd(current_path,line)
    elif "dir" in line:
        current_path.add_subdirectory(line)
    elif "ls" in line:
        pass
    else:
        current_path.add_file(line)


def test_create_file_from_string():
    file = File("143562 nrwjb")
    assert type(file) == File
    assert file.name == "nrwjb"
    assert file.size == 143562

def test_add_file_to_directory():
    file = File("143562 nrwjb")
    root = Directory()
    root.add_file(file)
    assert root.files != []

def test_add_subdirectory():
    root = Directory()
    root.add_subdirectory("123")
    assert root.subdirectories["123"] 


        
if __name__ == '__main__':
    f = file_rows_to_list("inputs\input6.txt")

    test_create_file_from_string()
    test_add_file_to_directory()
    test_add_subdirectory()
