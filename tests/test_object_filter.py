import unittest
from meraki_cli.__main__ import _object_filter


LISTOFDICTS = [
    {'id': '1', 'name': 'THING1'},
    {'id': '2', 'name': 'THING2'},
    {'id': '100', 'name': 'OTHERTHING'},
    {'id': '200', 'name': 'OTHER200THING'},
    {'id': '300', 'name': 'ELSE'}
    ]


class TestObjectFilter(unittest.TestCase):

    def testObjectFilterNotListError(self):
        # Should throw a log error since listofdicts input is not a list
        with self.assertLogs(level='ERROR'):
            _object_filter(LISTOFDICTS[0], ['goingToErorAnyways'])

    def testObjectFilterKeyMissingError(self):
        # Should throw a KeyError since we provided a bad key for the filter
        with self.assertRaises(KeyError):
            _object_filter(LISTOFDICTS, ['badkey:something'])

    def testObjectFilterNonFilter(self):
        # Should return nothing if filter list is empty
        output = _object_filter(LISTOFDICTS, [])
        assert output == []

    def testObjectFilterSimple(self):
        # Should return OTHERTHING, but nothing else
        output = _object_filter(LISTOFDICTS, ['name:OTHERTHING'])
        assert output == [LISTOFDICTS[2]]

    def testObjectFilterSimpleRegex(self):
        # Should return THING1 and THING2
        output = _object_filter(LISTOFDICTS, ['name:THING.'])
        assert output == LISTOFDICTS[0:2]

    def testObjectFilterOr(self):
        # Should return THING1 and OTHERTHING
        output = _object_filter(LISTOFDICTS,
                                ['name:THING1', 'name:OTHERTHING'])
        assert output == [LISTOFDICTS[0], LISTOFDICTS[2]]

    def testObjectFilterMultiKeyOr(self):
        # Should return THING1, THING2, and OTHER200THING
        output = _object_filter(LISTOFDICTS,
                                ['name:THING.', 'id:200'])
        assert output == LISTOFDICTS[0:2] + [LISTOFDICTS[3]]

    def testObjectFilterAnd(self):
        # Should return OTHERTHING and OTHER200THING
        output = _object_filter(LISTOFDICTS,
                                ['name:THING', 'id:...'], and_logic=True)
        assert output == LISTOFDICTS[2:4]
