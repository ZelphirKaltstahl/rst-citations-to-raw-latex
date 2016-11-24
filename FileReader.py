class FileReader():
    """reads files and returns their contents as line arrays"""

    def __init__(self):
        super().__init__()

    def read_file(self, file_path):
        lines = []
        print('now reading file', file_path)
        with open(file_path, mode='rU') as opened_file:
            # opened_file.seek(0)
            for line in opened_file:
                lines.append(opened_file.readline().rstrip('\n'))
        return lines
