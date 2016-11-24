class FileReader():
    """reads files and returns their contents as line arrays"""

    def __init__(self):
        super().__init__()

    def read_file(self, file_path):
        lines = []
        print('now reading file', file_path)
        with open(file_path, mode='rU') as opened_file:
            lines = opened_file.read().splitlines()
        return lines
