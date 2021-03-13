import unittest
import tempfile
import os
from .ParsedArgs import ParsedArgs
from meraki_cli.__main__ import _args_from_file


class TestArgsFromFile(unittest.TestCase):

    def setUp(self):
        self.parsed_args = ParsedArgs()

    def testArgsFromFileExplicitPathNoExist(self):
        self.parsed_args.configFile = '~/idontexist.conf'
        with self.assertLogs(level='CRITICAL'):
            with self.assertRaises(SystemExit):
                _args_from_file(self.parsed_args)

    def testArgsFromFileGoodPath(self):
        # If an env variable exists, delete it so it doesn't interfere
        if os.environ.get('MERAKI_DASHBOARD_API_KEY'):
            del os.environ['MERAKI_DASHBOARD_API_KEY']
        file = tempfile.NamedTemporaryFile('w', delete=False)
        file.write('{"apiKey": "abcdef"}')
        file.close()
        self.parsed_args.configFile = file.name
        _args_from_file(self.parsed_args)
        os.remove(file.name)
        assert self.parsed_args.apiKey == 'abcdef'

    def testArgsFromFileExplicitPathSuccess(self):
        # Create a temp meraki.conf file in the current dir
        configFile = open(os.path.join(os.getcwd(), 'meraki-cli.conf'), 'w')
        configFile.write('{"logfile": "expathtest.log"}')
        configFile.close()
        _args_from_file(self.parsed_args)
        os.remove(configFile.name)  # Delete that temp file
        assert self.parsed_args.logfile == 'expathtest.log'

    def testArgsFromFileEnvPath(self):
        folder = tempfile.TemporaryDirectory()
        # Set the APPDATA env var so we can test with it
        os.environ['APPDATA'] = folder.name
        # Create a ./meraki/ directory in the temp directory
        mdir = os.path.join(folder.name, 'meraki-cli')
        os.mkdir(mdir)
        # Create a ./meraki/meraki.conf temp config file
        configFile = open(os.path.join(mdir, 'meraki-cli.conf'), 'w')
        configFile.write('{"logfile": "envpathtest.log"}')
        configFile.close()
        _args_from_file(self.parsed_args)
        # Delete that env var
        del os.environ['APPDATA']
        assert self.parsed_args.logfile == 'envpathtest.log'
