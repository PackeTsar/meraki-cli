import unittest
from meraki_cli.__main__ import _cmd_title


class TestHelps(unittest.TestCase):

    def testTitle(self):
        assert _cmd_title('oneTwoThree') == 'One Two Three'
        assert _cmd_title('OneTwoThree') == 'One Two Three'
        assert _cmd_title('onetwoThree') == 'Onetwo Three'
