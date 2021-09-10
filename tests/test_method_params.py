import unittest
from unittest.mock import patch
from .ParsedArgs import ParsedArgs
from .Function import Function, ListFunction
from meraki_cli.__main__ import Args, _get_method_params


class TestMethodParams(unittest.TestCase):

    def setUp(self):
        self.parsed_args = ParsedArgs()
        self.arg_obj = Args(Function)
        self.arg_dict = {'pos1': '100', 'pos2': 200}

    # Adjust the NO_STDIN global to be true so program ignores all STDIN
    @patch('meraki_cli.__main__.NO_STDIN', True)
    def testMethodParamsSuccess(self):
        output = _get_method_params(self.parsed_args, self.arg_dict,
                                    self.arg_obj)
        assert output == (['100', 200], {'address': '192.168.1.1'})

    @patch('meraki_cli.__main__.NO_STDIN', True)
    def testMethodParamsBadKwargsError(self):
        self.parsed_args.kwargs = 'Some Bad JSON here'
        with self.assertRaises(SystemExit):
            _get_method_params(self.parsed_args, self.arg_dict,
                               self.arg_obj)

    def testMethodParamsMissingArgError(self):
        arg_dict = {'pos1': '100'}  # Should error due to missing required arg
        with self.assertLogs(level='CRITICAL'):
            with self.assertRaises(SystemExit):
                _get_method_params(self.parsed_args, arg_dict, self.arg_obj)

    @patch('meraki_cli.__main__.NO_STDIN', True)
    def testMethodParamsSimplePositional(self):
        # Clear kwargs entry to simplify output (no keyword args)
        self.parsed_args.kwargs = None
        # A JSON string is provided in a positional argument
        self.arg_dict['pos1'] = '["X1", "X2"]'
        assert self.arg_obj.positionals[0].annotation is str
        assert self.arg_obj.positionals[1].annotation is int
        output = _get_method_params(self.parsed_args, self.arg_dict,
                                    self.arg_obj)
        # NOTE: The Function arg "pos1" is a string type, so we shouldn't
        #     parse the CLI string as JSON
        assert output == (['["X1", "X2"]', 200], {})

    @patch('meraki_cli.__main__.NO_STDIN', True)
    def testMethodParamsComplexPositional(self):
        # A JSON string is provided in a positional argument
        self.arg_dict['pos1'] = '["X1", "X2"]'
        arg_obj = Args(ListFunction)
        assert arg_obj.positionals[0].annotation is list
        assert arg_obj.positionals[1].annotation is int
        output = _get_method_params(self.parsed_args, self.arg_dict,
                                    arg_obj)
        # NOTE: The ListFunction arg "pos1" is a list type, so we should
        #     parse the CLI string as JSON
        assert output == ([['X1', 'X2'], 200], {})

    @patch('meraki_cli.__main__.NO_STDIN', True)
    def testMethodParamsMalformedJSON(self):
        arg_obj = Args(ListFunction)
        self.arg_dict['pos1'] = '["X1"", "X2"]'
        output = _get_method_params(self.parsed_args, self.arg_dict,
                                    arg_obj)
        assert output == (['["X1"", "X2"]', 200], {})

    @patch('meraki_cli.__main__.NO_STDIN', True)
    def testMethodParamsNestedInListJSON(self):
        arg_obj = Args(ListFunction)
        self.arg_dict['pos1'] = ['["X1", "X2"]']
        output = _get_method_params(self.parsed_args, self.arg_dict,
                                    arg_obj)
        assert output == ([['X1', 'X2'], 200], {})

    @patch('meraki_cli.__main__.NO_STDIN', True)
    def testMethodParamsMalformedNestedInListJSON(self):
        arg_obj = Args(ListFunction)
        self.arg_dict['pos1'] = ['["X1"", "X2"]']
        output = _get_method_params(self.parsed_args, self.arg_dict,
                                    arg_obj)
        assert output == ([['["X1"", "X2"]'], 200], {})

    @patch('meraki_cli.__main__.NO_STDIN', True)
    def testMethodParamsMultiEntryList(self):
        arg_obj = Args(ListFunction)
        self.arg_dict['pos1'] = ['X1', 'X2']
        output = _get_method_params(self.parsed_args, self.arg_dict,
                                    arg_obj)
        assert output == ([['X1', 'X2'], 200], {})
