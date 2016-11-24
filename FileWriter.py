import os

class FileWriter():
    """writes resulting rst files"""

    def __init__(self):
        super().__init__()

    def write(self, rst_out_file_path, rst_file_content):
        with open(rst_out_file_path, 'w') as opened_file:
            opened_file.write(os.linesep.join(rst_file_content))
