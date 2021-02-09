import unittest
from meraki_cli.__main__ import _column_filter


LISTOFDICTS = [{
        'key1': 1,
        'key2': 2,
        'key3': 3,
        'key4': 4,
    }
]


class TestColumnFilter(unittest.TestCase):

    def test_ColumnFilter(self):
        output = _column_filter(LISTOFDICTS, 'key3,key2,key100')
        assert list(output[0]) == ['key3', 'key2']
        assert output == [{'key3': 3, 'key2': 2}]
