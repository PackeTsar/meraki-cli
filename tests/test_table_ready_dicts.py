import unittest
from meraki_cli.__main__ import _table_ready_dicts


LISTOFDICTS = [{
        'flatkey1': 1,
        'flatkey2': 2,
        'complexkey': [],
    }
]

# For testing output of a nested list of dicts like
#     when using appliance getNetworkApplianceFirewallL3FirewallRules
NESTEDLISTOFDICTS = {
    'items': LISTOFDICTS
}


class TestTableReadyDicts(unittest.TestCase):

    def testTableReadyDictsOutput(self):
        assert _table_ready_dicts(LISTOFDICTS) == [{
                'flatkey1': '1',
                'flatkey2': '2',
            }]

    def testTableReadyDictsNestedOutput(self):
        assert _table_ready_dicts(NESTEDLISTOFDICTS) == [{
                'flatkey1': '1',
                'flatkey2': '2',
            }]

    def testTableReadyDictsLogging(self):
        with self.assertLogs(level='DEBUG'):
            _table_ready_dicts(LISTOFDICTS)
