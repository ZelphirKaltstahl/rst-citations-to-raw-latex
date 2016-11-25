class FileReader():
    """reads files and returns their contents as line arrays"""

    def __init__(self):
        super().__init__()

    def read_file(self, file_path):
        # print('reading file:', file_path)
        lines = []
        with open(file_path, mode='rU') as opened_file:
            lines = opened_file.read().splitlines()

        # print('====================')
        # print('ORIGINAL FILE CONTENT (LINES)')
        # for lineno, line in enumerate(lines):
        #     print('LINE ' + str(lineno) + ':' + line)
        # print('====================')
        return lines
