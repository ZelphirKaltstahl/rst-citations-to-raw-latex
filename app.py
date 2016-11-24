import sys

import RSTCitations.FileReader as FileReader
import RSTCitations.BibParser as BibParser
import RSTCitations.RSTCitationParser as RSTCitationParser

class App():
    """application class"""

    def __init__(self):
        super().__init__()

        self.rst_parser = RSTCitationParser.RSTCitationParser()
        self.file_reader = FileReader.FileReader()
        self.bib_parser = BibParser.BibParser()

    def parse(self, rst_file_path, bib_file_path):
        rst_file_content = self.file_reader.read_file(rst_file_path)
        references = self.bib_parser.parse(bib_file_path)
        rst_file_content = self.rst_parser.add_raw_latex_rst_role(
            rst_file_content
        )
        self.rst_parser.parse(rst_file_content, references)


def print_help():
    print('call syntax:')
    print('python <program> <rst file> <bib file>')


def main(params):
    if len(params) != 3:
        print_help()
    else:
        rst_file_path = params[1]
        bib_file_path = params[2]
        app = App()
        app.parse(rst_file_path, bib_file_path)


if __name__ == '__main__':
    main(sys.argv)
