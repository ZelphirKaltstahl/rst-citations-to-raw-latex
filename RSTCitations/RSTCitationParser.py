import re


class RSTCitationParser():
    """parses rst files and exchanges citations with latex citations"""

    def __init__(self):
        super().__init__()
        self.citation_regex = re.compile(
            r"""
            [\s|^]*
            \[                 # literal [
            (?P<inner>         # named group 'inner' start
            [a-zA-Z0-9_., ]+   # allowed chars
            )                  # named group end
            \]                 # literal ]
            _                  # literal _
            """, re.VERBOSE)
        self.citation_no_extra = re.compile(
            r"""
            [\s|^]*
            \[
            (?P<citation_key>[a-zA-Z0-9_]+)
            \]
            _
            """, re.VERBOSE
        )
        self.citation_with_page_number = re.compile(
            r"""
            [\s|^]*
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
        self.citation_with_other_extra = re.compile(
            r"""
            [\s|^]*
            \[
            (?P<citation_key>[a-zA-Z_]+[0-9]+)
            [,]?
            [ ]+
            (?P<other_extra>[a-zA-Z0-9 -.]+)
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

        if self.citation_no_extra.match(' [swan_interactivity_2001]_'):
            print('no extra matches!')

        for one_match in matches:
            print('found a match:|', one_match.group() ,'|', sep='')
            if self.citation_no_extra.match(one_match.group()):
                print('no extra matches')
                line = self.replace_citation_no_extra_match(line, one_match)
            elif self.citation_with_page_number.match(one_match.group()):
                print('with page number matches')
                line = self.replace_citation_with_page_numbers(line, one_match)
            elif self.citation_with_other_extra.match(one_match.group()):
                print('with other extra matches')
                line = self.replace_citation_with_other_extra(line, one_match)
            else:
                print('"' + one_match.group() + '"')
                print('citation is an unknown style of citation')
        return line

    def replace_citation_no_extra_match(self, line, one_match):
        citation_key = \
            self.citation_no_extra \
                .match(one_match.group()) \
                .group('citation_key')
        latex_citation = self.create_latex_citation(citation_key, language='DE')
        rst_raw_latex_citation = self.latex_citation_to_rst_raw_latex_citation(
            latex_citation,
            one_match
        )
        return line.replace(one_match.group(), rst_raw_latex_citation)

    def replace_citation_with_page_numbers(self, line, one_match):
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
            page_number=page_number,
            language='DE'
        )
        rst_raw_latex_citation = self.latex_citation_to_rst_raw_latex_citation(
            latex_citation,
            one_match
        )
        return line.replace(one_match.group(), rst_raw_latex_citation)

    def replace_citation_with_other_extra(self, line, one_match):
        citation_key = \
            self.citation_with_other_extra \
            .match(one_match.group()) \
            .group('citation_key')

        other_extra = \
            self.citation_with_other_extra \
            .match(one_match.group()) \
            .group('other_extra')

        print('other extra is', other_extra)

        latex_citation = self.create_latex_citation(
            citation_key,
            other_extra=other_extra,
            language='DE'
        )

        print('latex_citation is', latex_citation)

        rst_raw_latex_citation = self.latex_citation_to_rst_raw_latex_citation(
            latex_citation,
            one_match
        )
        return line.replace(one_match.group(), rst_raw_latex_citation)

    def create_latex_citation(self, citation_key, page_number=None, other_extra=None, language='DE'):
        if language == 'EN':
            page_abbreviation = 'p.'
        elif language == 'DE':
            page_abbreviation = 'S.'
        else:
            page_abbreviation = 'p.'

        extra = ""
        if page_number:
            extra += ''.join([page_abbreviation, '~', page_number])

        if other_extra:
            extra += other_extra

        if page_number or other_extra:
            return '\cite[' + extra + ']{' + citation_key + '}'
        else:
            return '\cite{' + citation_key + '}'

    def latex_citation_to_rst_raw_latex_citation(
        self,
        latex_citation,
        one_match
    ):
        return one_match.group()[0] + ':raw-latex:`' + latex_citation + '`'
