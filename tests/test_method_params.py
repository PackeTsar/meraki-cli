import unittest
from .ParsedArgs import ParsedArgs
from .Function import Function
from meraki_cli.__main__ import Args, _get_method_params


class TestMethodParams(unittest.TestCase):

    def setUp(self):
        self.parsed_args = ParsedArgs()
        self.arg_obj = Args(Function)

    def testMethodParamsSuccess(self):
        arg_dict = {'pos1': '100', 'pos2': 200}
        output = _get_method_params(self.parsed_args, arg_dict, self.arg_obj)
        assert output == (['100', 200], {})

    def testMethodParamsError(self):
        arg_dict = {'pos1': '100'}
        with self.assertRaises(SystemExit):
            _get_method_params(self.parsed_args, arg_dict, self.arg_obj)
