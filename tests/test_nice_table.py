import unittest
from unittest.mock import patch
from io import StringIO
from meraki_cli.__main__ import _nice_table


LISTOFDICTS = [{
        'key1': '1',
        'key2': '1',
    }
]


class TestNiceTable(unittest.TestCase):

    def testNiceTableEmptyError(self):
        with self.assertLogs(level='WARNING'):
            with self.assertRaises(SystemExit):
                _nice_table([])

    def testNiceTableSuccess(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            _nice_table(LISTOFDICTS)
            self.assertIn('key1', fake_out.getvalue())
