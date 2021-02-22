"""
A basic class to instantiate and act like the parsed_args object
"""


class ParsedArgs:
    def __init__(self):
        self.type = 'organization'
        self.command = 'getOrganizationNetworks'
        self.debug = 0
        self.logfile = None
        self.networkId = 'N_12345'
        self.kwargs = '{"address": "192.168.1.1"}'
        self.jsonOutput = False
        self.columns = None
        self.apiKey = None
        self.configFile = None
