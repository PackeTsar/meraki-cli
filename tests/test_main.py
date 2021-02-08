import unittest
from meraki_cli.__main__ import main


class TestMain(unittest.TestCase):

    def testmain(self):
        with self.assertRaises(SystemExit):
            main()
