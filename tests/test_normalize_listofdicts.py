import unittest
from meraki_cli.__main__ import _normalize_listofdicts


COMPLETE_LIST = [
    {
        'key1': '1',
        'key2': '2',
    },
    {
        'key1': '3',
        'key2': '4',
    },
]

INCOMPLETE_LIST = [
    {
        'key1': '1',
        'key2': '2',
    },
    {
        'key0': '0',
        'key1': '3',
        'key2': '4',
    },
]

FIXED_INCOMPLETE_LIST = [
    {
        'key0': '',
        'key1': '1',
        'key2': '2',
    },
    {
        'key0': '0',
        'key1': '3',
        'key2': '4',
    },
]


class TestNormalizeListOfDicts(unittest.TestCase):

    def testNormalizeListOfDictsEmptyInput(self):
        with self.assertLogs(level='INFO'):
            output = _normalize_listofdicts([])
            assert output == []

    def testNormalizeListOfDictsNotAList(self):
        with self.assertLogs(level='INFO'):
            output = _normalize_listofdicts({'key0': '0'})
            assert output == {'key0': '0'}

    def testNormalizeListOfDictsEntryNotDict(self):
        with self.assertLogs(level='INFO'):
            output = _normalize_listofdicts(['1'])
            assert output == ['1']

    def testNormalizeListOfDictsCompleteDict(self):
        output = _normalize_listofdicts(COMPLETE_LIST)
        assert output == COMPLETE_LIST

    def testNormalizeListOfDictsIncompleteDict(self):
        output = _normalize_listofdicts(INCOMPLETE_LIST)
        assert output == FIXED_INCOMPLETE_LIST
