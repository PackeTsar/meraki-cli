import unittest
import inspect
from .Function import Function
from meraki_cli.__main__ import Args


class TestArgsClass(unittest.TestCase):

    def setUp(self):
        # Call function to exercise code and make testing coverage happy
        Function('', 0)
        self.args = Args(Function)

    def testPositionals(self):
        """
        Test Positional Parameters
        """
        assert len(self.args.positionals) == 2
        assert type(self.args.positionals) is list
        assert self.args.positionals[0].name == 'pos1'
        assert self.args.positionals[0].annotation is str
        assert self.args.positionals[0].default == inspect._empty
        assert self.args.positionals[1].name == 'pos2'
        assert self.args.positionals[1].annotation is int
        assert self.args.positionals[1].default == inspect._empty

    def test_keywords(self):
        assert len(self.args.keywords) == 2
        assert type(self.args.keywords) is list
        assert self.args.keywords[0].name == 'keyw1'
        assert self.args.keywords[0].annotation == inspect._empty
        assert self.args.keywords[0].default is False
        assert self.args.keywords[1].name == 'keyw2'
        assert self.args.keywords[1].annotation == inspect._empty
        assert self.args.keywords[1].default == {}

    def test_varargs(self):
        assert type(self.args.varargs) is inspect.Parameter
        assert self.args.varargs.name == 'args'
        assert self.args.varargs.annotation == inspect._empty
        assert self.args.varargs.default == inspect._empty

    def test_varkw(self):
        assert type(self.args.varkw) is inspect.Parameter
        assert self.args.varkw.name == 'kwargs'
        assert self.args.varkw.annotation == inspect._empty
        assert self.args.varkw.default == inspect._empty
