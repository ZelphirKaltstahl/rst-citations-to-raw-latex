import re


class RSTCitationParser():
    """parses rst files and exchanges citations with latex citations"""

    def __init__(self):
        super().__init__()
        self.citation_regex = re.compile(
            r"""
            [\s|^]+
            \[                 # literal [
            (?P<inner>         # named group 'inner' start
            [a-zA-Z0-9_., ]+   # allowed chars
            )                  # named group end
            \]                 # literal ]
            _                  # literal _
            """, re.VERBOSE)
        self.citation_no_extra = re.compile(
            r"""
            [\s|^]+
            \[
            (?P<citation_key>[a-zA-Z0-9_]+)
            \]
            _
            """, re.VERBOSE
        )
        self.citation_with_page_number = re.compile(
            r"""
            [\s|^]+
            \[
            (?P<citation_key>[a-zA-Z_]+[0-9]+)
            [,]?
            [ ]+
            [p|P|s|S]
            [.]
            [ ]?
            (?P<page_number>[0-9]+)
            \]
            _
            """, re.VERBOSE
        )

    def add_raw_latex_rst_role(self, rst_file_content):
        rst_file_content.insert(0, '')
        rst_file_content.insert(0, '   :format: latex')
        rst_file_content.insert(0, '.. role:: raw-latex(raw)')
        return rst_file_content

    def parse(self, rst_file_content):
        for lineno, line in enumerate(rst_file_content):
            all_matches = list(re.finditer(self.citation_regex, line))
            if all_matches:
                line = self.replace_matches(line, all_matches)
                rst_file_content[lineno] = line
        return rst_file_content

    def replace_matches(self, line, matches):
        for one_match in matches:
            if self.citation_no_extra.match(one_match.group()):
                citation_key = \
                    self.citation_no_extra \
                    .match(one_match.group()) \
                    .group('citation_key')

                latex_citation = self.create_latex_citation(
                    citation_key
                )
                rst_raw_latex_citation = self.latex_citation_to_rst_raw_latex_citation(
                    latex_citation,
                    one_match
                )
                line = line.replace(one_match.group(), rst_raw_latex_citation)

            elif self.citation_with_page_number.match(one_match.group()):
                citation_key = \
                    self.citation_with_page_number \
                    .match(one_match.group()) \
                    .group('citation_key')

                page_number = \
                    self.citation_with_page_number \
                    .match(one_match.group()) \
                    .group('page_number')

                latex_citation = self.create_latex_citation(
                    citation_key,
                    page_number
                )
                rst_raw_latex_citation = self.latex_citation_to_rst_raw_latex_citation(
                    latex_citation,
                    one_match
                )
                line = line.replace(one_match.group(), rst_raw_latex_citation)
            else:
                print('"' + one_match.group() + '"')
                print('citation is an unknown style of citation')

        return line

    def create_latex_citation(self, citation_key, page_number=None):
        if page_number:
            return '\cite[p.~' + page_number + ']{' + citation_key + '}'
        else:
            return '\cite{' + citation_key + '}'

    def latex_citation_to_rst_raw_latex_citation(
        self,
        latex_citation,
        one_match
    ):
        return one_match.group()[0] + ':raw-latex:`' + latex_citation + '`'
