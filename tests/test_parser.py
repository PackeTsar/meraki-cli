import unittest
from meraki_cli.__main__ import Parser


class TestParser(unittest.TestCase):

    def testParser(self):
        parser = Parser()
        parser.add_argument('--test')
        with self.assertLogs(level='CRITICAL'):
            with self.assertRaises(SystemExit):
                # Parse with bad CLI arguments to force a failure
                parser.parse_args('test')
