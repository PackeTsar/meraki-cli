import unittest
import logging
from meraki_cli.__main__ import _configure_logging


class TestLogger(unittest.TestCase):

    def setUp(self):
        # Create a namespace object with a couple parameters used in the func
        self.parsed_args = type('', (), {'debug': 2, 'logfile': None})()
        self.logger = logging.getLogger('testing')
        self.output = _configure_logging(self.parsed_args)

    def testParsedArgs(self):
        assert self.parsed_args.debug == 2
        assert self.parsed_args.logfile is None

    def testLoggerOutput(self):
        assert type(self.output) is tuple
        assert len(self.output) == 2
        assert type(self.output[0]) is logging.Logger
        assert type(self.output[1]) is logging.Logger
