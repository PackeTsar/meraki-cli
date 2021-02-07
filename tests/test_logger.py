import unittest
import logging
import os
from meraki_cli.__main__ import _configure_logging


class TestLogger(unittest.TestCase):

    def setUp(self):
        # Create a namespace object with a parameters used in the func and
        #     run function to test code paths
        self.parsed_argsv1 = type('', (), {'debug': 1, 'logfile': None})()
        self.parsed_argsv2 = type('', (), {'debug': 2, 'logfile': None})()
        self.parsed_argsv3 = type('', (), {'debug': 3, 'logfile': 'log.log'})()
        self.logger = logging.getLogger('testing')
        self.outputv1 = _configure_logging(self.parsed_argsv1)
        self.outputv2 = _configure_logging(self.parsed_argsv2)
        self.outputv2 = _configure_logging(self.parsed_argsv3)

    def testParsedArgs(self):
        assert self.parsed_argsv1.debug == 1
        assert self.parsed_argsv1.logfile is None
        assert self.parsed_argsv2.debug == 2
        assert self.parsed_argsv2.logfile is None
        assert self.parsed_argsv3.debug == 3
        assert self.parsed_argsv3.logfile == 'log.log'

    def testLoggerOutputV1(self):
        assert type(self.outputv1) is tuple
        assert len(self.outputv1) == 2  # output is (log, meraki_log)
        assert type(self.outputv1[0]) is logging.Logger
        assert type(self.outputv1[1]) is logging.Logger

    def testLogFile(self):
        """
        Was the logfile created? It should have been when we instantiated the
            logger in the function with a logfile defined.
        """
        assert os.path.isfile('log.log')  # Was the logfile created?
