import unittest
from meraki_cli.__main__ import main


"""
NOTE: You may get the below failure if you have a config file existing when
    you run the testing suite

OSError: pytest: reading from stdin while output is captured!
"""


class TestMain(unittest.TestCase):

    def testmain(self):
        with self.assertRaises(SystemExit):
            main()
        with self.assertRaises(SystemExit):
            main('organizations')
        with self.assertRaises(SystemExit):
            main('organizations getOrganizations -h')
