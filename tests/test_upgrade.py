import unittest
from unittest.mock import patch
from .ParsedArgs import ParsedArgs
from meraki_cli.__main__ import _upgrade


def check_prompt(prompt):
    if 'Continue' not in prompt:
        raise Exception('Confirmation prompt is broken!')
    return 'y'


class TestUpgrade(unittest.TestCase):

    def setUp(self):
        """
        Add the needed arguments to the simulated parser
        """
        self.parsed_args = ParsedArgs()
        self.parsed_args.no_confirm = True
        self.parsed_args.upgrade_all = False
        self.parsed_args.upgrade_meraki_cli = False
        self.parsed_args.upgrade_meraki_sdk = False
        self.parsed_args.upgrade_all_eager = False

    def testUpgradeAll(self):
        self.parsed_args.upgrade_all = True
        _upgrade(self.parsed_args)

    def testUpgradeCLIOnly(self):
        self.parsed_args.upgrade_meraki_cli = True
        _upgrade(self.parsed_args)

    def testUpgradeSDKOnly(self):
        self.parsed_args.upgrade_meraki_sdk = True
        _upgrade(self.parsed_args)

    # Replace input() with our check_prompt function
    @patch('builtins.input', check_prompt)
    def testUpgradeConfirm(self):
        self.parsed_args.no_confirm = False
        self.parsed_args.upgrade_meraki_cli = True
        _upgrade(self.parsed_args)

    # Replace input() with our function with one that just returns 'n'
    @patch('builtins.input', lambda _: 'n')
    def testUpgradeCancel(self):
        self.parsed_args.no_confirm = False
        self.parsed_args.upgrade_meraki_cli = True
        # Make sure critical log throws
        with self.assertLogs(level='CRITICAL'):
            # Make sure system exits with code 1
            with self.assertRaises(SystemExit) as cm:
                _upgrade(self.parsed_args)
            self.assertEqual(cm.exception.code, 1)

    def testUpgradeHang(self):
        """
        Test that the program hangs and asks for user input. Don't patch
            the input() builtin function so it hangs asking for user input.
        """
        self.parsed_args.no_confirm = False
        self.parsed_args.upgrade_meraki_cli = True
        # OSError should be raised when input() is called within unit testing
        with self.assertRaises(OSError):
            _upgrade(self.parsed_args)
