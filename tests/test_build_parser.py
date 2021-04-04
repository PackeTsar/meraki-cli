import unittest
import meraki
from meraki_cli.__main__ import _build_parser, Parser


class TestBuildParser(unittest.TestCase):

    def testBuildParser(self):
        # Instantiate the fake API so we can analyze it
        api = meraki.DashboardAPI('fake_key', suppress_logging=True)
        parser = Parser(add_help=False)  # Create a parser instance
        # Put a subparser in it so we can populate that
        subparser = parser.add_subparsers(dest='type', title='Command Types')
        # Run the _build_parser to build out the info inside the parser
        _build_parser(subparser, api)
