import unittest
from meraki_cli.__main__ import _check_for_key


LISTOFDICTS = [
    {'id': '1', 'name': 'THING1'},
    {'id': '2', 'name': 'THING2'},
    {'id': '100', 'name': 'OTHERTHING'},
    {'id': '200', 'name': 'OTHER200THING'},
    {'id': '300', 'name': 'ELSE'}
]

INCONSISTENTKEYS = [
    {'k3': 'v3'},
    {'k1': 'v1', 'k2': 'v2'},
]


class TestCheckForKey(unittest.TestCase):

    def testCheckForKeyNonString(self):
        # Should raise an exception since the key is not a string
        with self.assertRaises(Exception):
            _check_for_key(LISTOFDICTS, [])

    def testCheckForKeyNoExist(self):
        # Should return False since this key IS NOT in LISTOFDICTS
        self.assertFalse(_check_for_key(LISTOFDICTS, 'doesntexist'))

    def testCheckForKeyExists(self):
        # Should return True since this key IS in LISTOFDICTS
        self.assertTrue(_check_for_key(LISTOFDICTS, 'name'))

    def testCheckForKeyInconsistentExists(self):
        # Should return true since this key is somewhere in INCONSISTENTKEYS
        self.assertTrue(_check_for_key(INCONSISTENTKEYS, 'k1'))

    def testCheckForKeyInconsistentNoExist(self):
        # Should return False and throw a warning since this key is not in
        #     the LISTOFDICTS.
        with self.assertLogs('testing', level='WARNING'):
            self.assertFalse(_check_for_key(LISTOFDICTS, 'kx'))
