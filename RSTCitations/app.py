import sys
import os.path

import RSTCitations.FileReader as FileReader
import RSTCitations.FileWriter as FileWriter
import RSTCitations.RSTCitationParser as RSTCitationParser


class App():
    """application class"""

    def __init__(self):
        super().__init__()

        self.rst_parser = RSTCitationParser.RSTCitationParser()
        self.file_reader = FileReader.FileReader()
        self.file_writer = FileWriter.FileWriter()

    def parse(self, rst_file_path):
        print('Now reading input file ...')
        rst_file_content = self.file_reader.read_file(rst_file_path)
        print('Parsing input file ...')
        rst_file_content = self.rst_parser.add_raw_latex_rst_role(
            rst_file_content
        )
        rst_file_content = self.rst_parser.parse(rst_file_content)
        print('Writing output file ...')
        self.file_writer.write(rst_file_path + '.out', rst_file_content)
        print('Successfully wrote output file.')


def print_help():
    print('call syntax:')
    print('python <program> <rst file>')


def main(params):
    if len(params) != 2:
        print_help()
    else:
        rst_file_path = params[1]
        if not os.path.isfile(rst_file_path):
            sys.exit('The file you specified does not exist or is not a file.')

        app = App()
        app.parse(rst_file_path)


if __name__ == '__main__':
    main(sys.argv)
