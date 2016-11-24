class BibParser():
    """parses bib files and returns references as lists of dictionaries"""

    def __init__(self):
        super().__init__()

    def parse(self, bib_file_path):
        print('BibParser parsing bib file:', bib_file_path)
        # TODO
        return [{
            'type': 'article',
            'citation_key': 'chou_interactivity_2003',
            'title': 'Interactivity and interactive functions in web-based learning systems: a technical framework for designers',
            'author': 'Chou, Chien',
            'journal': 'British Journal of Educational Technology',
            'volume': 34,
            'number': 3,
            'pages': '265--279',
            'year': 2003,
            'publisher': 'Wiley Online Library'
        }]
