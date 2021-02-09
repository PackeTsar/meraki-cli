import unittest
from unittest.mock import patch
from io import StringIO
import json
from .ParsedArgs import ParsedArgs
from meraki_cli.__main__ import _output


LISTOFDICTS = [{
        'key1': '1',
        'key2': '1',
        'badkey': [],
    }
]


class TestOutput(unittest.TestCase):

    def setUp(self):
        self.parsed_args = ParsedArgs()

    def testOutputEmptyResult(self):
        with self.assertLogs(level='INFO'):
            output = _output(self.parsed_args, [])
        assert output is None

    @patch('meraki_cli.__main__.NO_STDOUT', True)
    def testOutputJsonSwitch(self):
        self.parsed_args.jsonOutput = True
        with patch('sys.stdout', new=StringIO()) as fake_out:
            _output(self.parsed_args, LISTOFDICTS)
            assert json.loads(fake_out.getvalue()) == LISTOFDICTS

    @patch('meraki_cli.__main__.NO_STDOUT', False)
    def testOutputJsonStdout(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            _output(self.parsed_args, LISTOFDICTS)
            assert json.loads(fake_out.getvalue()) == LISTOFDICTS

    @patch('meraki_cli.__main__.NO_STDOUT', True)
    def testOutputNonList(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            _output(self.parsed_args, LISTOFDICTS[0])
            stdout = fake_out.getvalue()
            self.assertIn('key1', stdout)

    @patch('meraki_cli.__main__.NO_STDOUT', True)
    def testOutputRemovedColumn(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.parsed_args.columns = 'key2'
            _output(self.parsed_args, LISTOFDICTS)
            self.assertNotIn('key1', fake_out.getvalue())
