import unittest
import tempfile
import os
from .ParsedArgs import ParsedArgs
from meraki_cli.__main__ import _reconcile_args


class TestReconcileArgs(unittest.TestCase):

    def tearDown(self):
        if 'file' in self.__dict__:
            os.remove(self.file.name)

    def _getArgsAndFile(self, fileContents: str):
        self.file = tempfile.NamedTemporaryFile('w', delete=False)
        self.file.write(fileContents)
        self.file.close()
        return ParsedArgs(), self.file

    def testReconcileArgsBadJsonError(self):
        parsed_args, file = self._getArgsAndFile('')
        with self.assertLogs(level='CRITICAL'):
            with self.assertRaises(SystemExit):
                _reconcile_args(parsed_args, file.name)

    def testReconcileArgsNotDictError(self):
        parsed_args, file = self._getArgsAndFile('[]')
        with self.assertLogs(level='CRITICAL'):
            with self.assertRaises(SystemExit):
                _reconcile_args(parsed_args, file.name)

    def testReconcileArgsCommandArg(self):
        parsed_args, file = self._getArgsAndFile('{"command": "testcommand"}')
        _reconcile_args(parsed_args, file.name)
        assert parsed_args.command == 'testcommand'

    def testReconcileArgsUnrecognizedArgError(self):
        parsed_args, file = self._getArgsAndFile('{"badarg": null}')
        with self.assertLogs(level='CRITICAL'):
            with self.assertRaises(SystemExit):
                _reconcile_args(parsed_args, file.name)

    @unittest.mock.patch.dict(
        os.environ, {'MERAKI_DASHBOARD_API_KEY': '12345'})
    def testReconcileArgsApiKeyEnvVarPreferEnv(self):
        parsed_args, file = self._getArgsAndFile('{"apiKey": "6789"}')
        _reconcile_args(parsed_args, file.name)
        assert parsed_args.apiKey is None

    def testReconcileArgsApiKeyEnvVarFallback(self):
        # If an env variable exists, delete it so it doesn't interfere
        if os.environ.get('MERAKI_DASHBOARD_API_KEY'):
            del os.environ['MERAKI_DASHBOARD_API_KEY']
        parsed_args, file = self._getArgsAndFile('{"apiKey": "6789"}')
        _reconcile_args(parsed_args, file.name)
        assert parsed_args.apiKey == "6789"

    def testReconcileArgsSuccess(self):
        parsed_args, file = self._getArgsAndFile('{"jsonOutput": true}')
        _reconcile_args(parsed_args, file.name)
        assert parsed_args.jsonOutput is True
