import unittest
from .ParsedArgs import ParsedArgs
from meraki_cli.__main__ import _clean_args


class TestCleanArgs(unittest.TestCase):

    def testCleanArgs(self):
        assert _clean_args(ParsedArgs()) == {'networkId': 'N_12345'}
