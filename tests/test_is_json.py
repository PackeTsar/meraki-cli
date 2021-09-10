import unittest
from meraki_cli.__main__ import _is_json


class TestIsJSON(unittest.TestCase):

    def testIsJSONBadInput(self):
        self.assertFalse(_is_json({}))

    def testIsJSONFalse(self):
        self.assertFalse(_is_json('abcd'))

    def testIsJSONTrue(self):
        self.assertTrue(_is_json('["1", "2"]'))
