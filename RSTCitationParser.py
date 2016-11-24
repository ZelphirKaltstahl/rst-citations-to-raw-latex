import re


class RSTCitationParser():
    """parses rst files and exchanges citations with latex citations"""

    def __init__(self):
        super().__init__()
        self.citation_regex = re.compile(
            r"""
            \[                 # literal [
            (                  # group start
            [a-zA-Z0-9_. ]+    # allowed chars
            )                  # group end
            \]                 # literal ]
            """, re.VERBOSE)

    def add_raw_latex_rst_role(self, rst_file_content):
        rst_file_content.insert(0, '')
        rst_file_content.insert(0, '   :format: latex')
        rst_file_content.insert(0, '.. role:: raw-latex(raw)')
        return rst_file_content

    def parse(self, rst_file_content, references):
        print('findings:')
        for lineno, line in enumerate(rst_file_content):
            all_matches = re.findall(self.citation_regex, line)
            if all_matches:
                print(all_matches)

        # \cite[p.~150]{kopka2003guide}

        # TODO
        print('RSTCitationParser parsing:')
        print(rst_file_content)
        print(references)
