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

BAD_TRANSLATION = 'changed-changeme'  # Uses a minus 'accidently'


class TestTranslations(unittest.TestCase):

    def testTranslation(self):
        assert _translate_input(INPUT, ['changed=changeme']) == OUTPUT

    def testTranslationBadFormatLogThenExit(self):
        with self.assertLogs(level='CRITICAL'):
            with self.assertRaises(SystemExit):
                _translate_input(INPUT, BAD_TRANSLATION) == OUTPUT
