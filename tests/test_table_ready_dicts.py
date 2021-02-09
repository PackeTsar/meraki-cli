import unittest
from meraki_cli.__main__ import _table_ready_dicts


LISTOFDICTS = [{
        'flatkey1': 1,
        'flatkey2': 2,
        'complexkey': [],
    }
]


class TestTableReadyDicts(unittest.TestCase):

    def testTableReadyDictsOutput(self):
        assert _table_ready_dicts(LISTOFDICTS) == [{
                'flatkey1': '1',
                'flatkey2': '2',
            }]

    def testTableReadyDictsLogging(self):
        with self.assertLogs(level='DEBUG'):
            _table_ready_dicts(LISTOFDICTS)
