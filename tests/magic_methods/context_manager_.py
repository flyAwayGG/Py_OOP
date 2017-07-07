class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        print(f'File {self.filename} opened with mode {self.mode}')
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()
        print(f'File {self.filename} closed')
        print(f"Total data in file: {open(self.filename,'r').readlines()}")
        print()



def test_():
    with File('foo.txt', 'a') as infile:
        for i in range(3):
            infile.write('foo'+str(i))

