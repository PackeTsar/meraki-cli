import unittest
from unittest.mock import patch
from io import StringIO
from .ParsedArgs import ParsedArgs
from .Function import Function
from meraki_cli.__main__ import Args, _print_commands


EXPECT = """
meraki organization getOrganizationNetworks --pos1 'positional1' --pos2 \
'positional2' --kwargs '{"key1": "value1"}' \


"""


class TestPrintCommands(unittest.TestCase):

    def setUp(self):
        self.parsed_args = ParsedArgs()
        self.arg_obj = Args(Function)
        # Turn this and the target method into a ready to use command
        self.arg_tup = [(['positional1', 'positional2'], {'key1': 'value1'})]

    @patch('sys.argv', ['meraki'])
    def testPrintCommands(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            _print_commands(self.parsed_args, self.arg_tup,
                            self.arg_obj)
            self.assertEqual(fake_out.getvalue(), EXPECT)
