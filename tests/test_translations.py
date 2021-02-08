import unittest
from meraki_cli.__main__ import _translate_input


INPUT = [
    {
        'changeme': '100',
        'leavemealone': '101'
    },
    {
        'changeme': '200',
        'leavemealone': '201'
    },
]

OUTPUT = [
    {
        'changed': '100',
        'leavemealone': '101'
    },
    {
        'changed': '200',
        'leavemealone': '201'
    },
]


class TestTranslations(unittest.TestCase):

    def testTranslation(self):
        assert _translate_input(INPUT, ['changed=changeme']) == OUTPUT
