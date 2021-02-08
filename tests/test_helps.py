import unittest
from .Function import Function
from meraki_cli.__main__ import Args, _cmd_title, _cmd_help


class TestHelps(unittest.TestCase):

    def testTitle(self):
        assert _cmd_title('oneTwoThree') == 'One Two Three'
        assert _cmd_title('OneTwoThree') == 'One Two Three'
        assert _cmd_title('onetwoThree') == 'Onetwo Three'
