import unittest
from unittest.mock import patch
from io import StringIO
import json
from .ParsedArgs import ParsedArgs
from .Function import Function
from meraki_cli.__main__ import Args, _json_to_args, _get_stdin_args


# Using a dict and not a list to check the it converts to list
JSON_DATA = '{"willbepos1": "100", "pos2": 200}'


class TestStdin(unittest.TestCase):

    def setUp(self):
        self.parsed_args = ParsedArgs()
        self.parsed_args.translations = ['pos1=willbepos1']
        self.arg_obj = Args(Function)
        self.proper_output = [(['100', 200], {'networkId': 'N_12345'})]

    # @patch added for Windows testing
    @patch('meraki_cli.__main__.NO_STDIN', False)
    def testJsonToArgs(self):
        # Pass the string directly to the argument first
        output = _json_to_args(JSON_DATA, self.parsed_args, self.arg_obj)
        assert output == self.proper_output

    @patch('sys.stdin', StringIO(''))
    def testStdinEmptyError(self):
        # Should try to read from STDIN and error out because it is empty
        with self.assertRaises(SystemExit):
            _get_stdin_args(self.parsed_args, self.arg_obj)

    @patch('sys.stdin', StringIO('bad JSON data'))
    def testStdinBadJson(self):
        # Should try to read from STDIN and error out because it is improperly
        #     formatted JSON data
        with self.assertRaises(json.decoder.JSONDecodeError):
            _get_stdin_args(self.parsed_args, self.arg_obj)

    @patch('sys.stdin', StringIO(JSON_DATA))
    # @patch added for Windows testing
    @patch('meraki_cli.__main__.NO_STDIN', False)
    def testStdinSuccess(self):
        # Should try to read from STDIN and succeed because it is properly
        #     formatted JSON data
        output = _get_stdin_args(self.parsed_args, self.arg_obj)
        assert output == self.proper_output
