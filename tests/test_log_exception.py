import unittest
from unittest.mock import patch
import logging
from meraki_cli.__main__ import _log_exception


class TestLogException(unittest.TestCase):

    @patch('meraki_cli.__main__.log.level', logging.INFO)
    def testLogException(self):
        with self.assertLogs(level='CRITICAL'):
            assert _log_exception(Exception('Some Message Here')) is None

    def testLogExceptionExit(self):
        with self.assertRaises(SystemExit):
            _log_exception(Exception('Some Message Here'), exit=True)
