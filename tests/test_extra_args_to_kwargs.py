import unittest
from meraki_cli.__main__ import _extra_args_to_kwargs


class TestExtraArgsToKwargs(unittest.TestCase):

    def testEmptyEmpty(self):
        assert _extra_args_to_kwargs({}, []) == {}

    def testEmptyArgList(self):
        existing_kwarg_dict = {'arg1': 1, 'arg2': '2'}
        result = _extra_args_to_kwargs(existing_kwarg_dict, [])
        assert result == existing_kwarg_dict

    def testArgListWithoutExistingKwargs(self):
        result = _extra_args_to_kwargs({}, [
            '--vlan',
            '100',
            '--name',
            'somename'
        ])
        assert result == {
            'vlan': '100',
            'name': 'somename'
        }

    def testArgListWithExistingKwargs(self):
        result = _extra_args_to_kwargs(
            {
                'origarg': 'origvalue',
            },
            [
                '--vlan',
                '100',
                '--name',
                'somename'
            ])
        assert result == {
            'vlan': '100',
            'name': 'somename',
            'origarg': 'origvalue',
            }

    def testNestedData(self):
        result = _extra_args_to_kwargs(
            {
                'origarg': 'origvalue',
            },
            [
                '--vlan',
                '{"nestedarg": "nestedvalue"}',
                '--name',
                'somename'
            ])
        assert result == {
            'vlan': {
                'nestedarg': 'nestedvalue',
            },
            'name': 'somename',
            'origarg': 'origvalue',
            }

    def testIncompleteArgs(self):
        with self.assertRaises(SystemExit):
            _extra_args_to_kwargs({}, [
                '--vlan',
                '100',
                '--name'
            ])

    def testComments(self):
        result = _extra_args_to_kwargs({}, [
            '--vlan',
            '100',
            '--name',
            'somename',
            '#',
            'Some',
            'comments',
            'here',
            '--lastarg',
            'lastvalue',
        ])
        assert result == {
            'vlan': '100',
            'name': 'somename',
            'lastarg': 'lastvalue',
        }
