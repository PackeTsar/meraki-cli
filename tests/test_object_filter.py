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

    def testObjectFilterEmptyList(self):
        output = _object_filter([], ['name:THING'])
        assert output == []

    def testObjectFilterKeyMissingWarning(self):
        # Should throw a warning since this key does not exist in any of
        #     the data
        with self.assertLogs(level='WARNING'):
            _object_filter(LISTOFDICTS, ['missing:key'])
        # Test with multiple filter keys, one of which is good. Make sure
        #     the warning still fires.
        with self.assertLogs(level='WARNING'):
            _object_filter(LISTOFDICTS, ['name:THING.', 'missing:key'])
        # Test with AND logic and make sure warning fires
        with self.assertLogs(level='WARNING'):
            _object_filter(LISTOFDICTS, ['name:THING.', 'missing:key'],
                           and_logic=True)

    def testObjectFilterKeyMissingReturn(self):
        # Should return an empty list since this key does not exist in any
        #     of the data.
        output = _object_filter(LISTOFDICTS, ['missing:key'])
        assert output == []
        # Test with multiple keys. Should return objects (using "OR" logic)
        output = _object_filter(LISTOFDICTS, ['name:THING.', 'missing:key'])
        assert output == LISTOFDICTS[0:2]
        # Test with multiple keys. Should return nothing (using "AND" logic)
        output = _object_filter(LISTOFDICTS, ['name:THING.', 'missing:key'],
                                and_logic=True)
        assert output == []

    def testObjectFilterKeyInconsistentData(self):
        # Create a listofdicts with inconsistent keys
        data = [
            {'k2': 'v2'},
            {'k1': 'v1', 'k2': 'v2'},
            {'k3': 'v3', 'k4': 'v4'},
        ]
        # Should return no warnings
        assert _object_filter(data, ['k1:v.']) == [data[1]]
        assert _object_filter(data, ['k1:v.'], and_logic=True) == []

    def testObjectFilterComplexData(self):
        # Test filtering complex values (dict). Should be flattened to str
        #     before filtering happens
        data = [
            {'k': {'test1': 'test1'}},
            {'k': {'test2': 'test2'}},
            {'k': {'test3': 'test3'}},
        ]
        assert _object_filter(data, ['k:test2']) == [data[1]]

    def testObjectFilterMalformedString(self):
        # Test that a malformed filter causes a SystemExit
        with self.assertRaises(SystemExit) as cm:
            # And throws an ERROR log
            with self.assertLogs(level='ERROR'):
                _object_filter(LISTOFDICTS, ['badfilter'])
        # And the exit code is 1 (error)
        self.assertEqual(cm.exception.code, 1)
