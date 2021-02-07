import unittest
from .Function import Function
from meraki_cli.__main__ import Args, _cmd_title, _cmd_help


class TestHelps(unittest.TestCase):

    def testTitle(self):
        assert _cmd_title('oneTwoThree') == 'One Two Three'
        assert _cmd_title('OneTwoThree') == 'One Two Three'
        assert _cmd_title('onetwoThree') == 'Onetwo Three'

    # def testHelp(self):
    #    value = '\n    Some function documentation here\n    \n'\
    #            '        >>> def Function(pos1: str, pos2: int, keyw1=False,'\
    #            ' keyw2={}, *args, **kwargs):'
    #    assert _cmd_help(Args(Function)) == value
