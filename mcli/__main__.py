#!/usr/bin/python


'''
Primary program file. Build/process CLI arguments here and call functions in
    other files as necessary
'''


# Built-in Libs
import sys
import json
import logging
import argparse

# Installed Libs
import meraki
import tabulate

# Custom Libs
from . import __version__
from .utilities import attrib_expression


log = logging.getLogger('meraki-cli')  # Our logging facility
mlog = logging.getLogger('meraki')  # Meraki library's facility
consoleHandler = logging.StreamHandler()  # Console output
log.addHandler(consoleHandler)
log.setLevel(logging.WARNING)  # Set to warning by default for us
mlog.setLevel(logging.WARNING)  # Set Meraki library to warning by default
logging.basicConfig(filename=None)  # Fix stupid Meraki library defaults


TABLECOLUMNS = []  # Global for listing columns to report out to tables


def showorgs(args, api):
    '''
    Command to list out organizations for API key
    Args: None
    '''
    # Set the global with columns we want to show
    TABLECOLUMNS.__iadd__(['id', 'name'])
    # Pull the data from Meraki
    orgs = api.organizations.getOrganizations()
    # Send to reporter to format and show to user
    reporter(args, orgs)


def showdevices(args, api):
    '''
    Command to list out devices for an organization
    Args:
        Required:
            '--org_id' or '-o'
    '''
    TABLECOLUMNS.__iadd__(['name', 'serial', 'model', 'lanIp'])
    devices = api.devices.getOrganizationDevices(organizationId=args.org_id)
    reporter(args, devices)


def showswitchports(args, api):
    '''
    Command to list out ports on a switch
    Args:
        Required:
            '--switch_serial' or '-s'
        Optional:
            '--port_name' or '-p': Limit output to one port
            '--status' or '-a': Show status instead of config
    '''
    if args.status:
        TABLECOLUMNS.__iadd__(['portId', 'enabled', 'status', 'speed', 'duplex',
                               'clientCount', 'trafficInKbps'])
        ports = api.switch_ports.getDeviceSwitchPortStatuses(
                serial=args.switch_serial)
    else:
        TABLECOLUMNS.__iadd__(['number', 'enabled', 'type', 'vlan',
                               'voiceVlan', 'allowedVlans', 'name'])
        if not args.port_name:
            ports = api.switch_ports.getDeviceSwitchPorts(
                serial=args.switch_serial)
        else:
            ports = api.switch_ports.getDeviceSwitchPort(
                serial=args.switch_serial, number=args.port_name)
    reporter(args, ports)


def updateswitchport(args, api):
    '''
    Command to update a switchport with new config attributes
    Args:
        Required:
            '--switch_serial' or '-s'
            '--port_name' or '-p'
            Positional Attribute Expressions (ie: 'vlan:200 type:access')
    '''
    TABLECOLUMNS.__iadd__(['number', 'enabled', 'type', 'vlan',
                           'voiceVlan', 'allowedVlans'])
    # Process attribute expressions through an interpreter
    newattribs = attrib_expression(args.attributes)
    update = api.switch_ports.updateDeviceSwitchPort(
            serial=args.switch_serial, number=args.port_name, **newattribs)
    reporter(args, [update])


def format_table(data):
    '''
    Reformat a list of dicts for use by tabulate library
    '''
    rows = []  # Output should be a list of lists, each internal list is a row
    for d in data:
        row = []  # Row represented as a list
        # Use the TABLECOLUMNS global to order cells in row
        for col in TABLECOLUMNS:
            try:  # Allow for inconsistent keys
                row.append(d[col])
            # If key doesn't exist, insert an empty entry
            except KeyError:
                row.append('')
        rows.append(row)  # Insert row into table
    return rows


def reporter(args, data):
    '''
    Format and print response data out to the user
    '''
    if args.table:  # Detect a request to output a table of data
        # Reformat data for tabulate required input
        rows = format_table(data)
        # Print table-formatted data
        console(tabulate.tabulate(rows, TABLECOLUMNS))
    else:
        # If table not requested, output pretty JSON
        console(json.dumps(data, indent=4))


def console(data):
    '''
    All output printed for user comes through here to avoid print()'s
    '''
    print(f'\n{data}\n')


def get_api(args):
    '''
    Grab the Meraki API object using the API key
    '''
    return meraki.DashboardAPI(api_key=args.api_key)


def set_debug_level(args):
    '''
    Detect debugging level set by user and set logging level
    '''
    if not args.debug:  # If no '-d' arguments
        return None
    elif args.debug == 1:  # If one '-d'
        log.setLevel(logging.INFO)
        mlog.setLevel(logging.INFO)
        log.debug('Logging level set to INFO')
    elif args.debug > 1:  # If '-dd' or more
        log.setLevel(logging.DEBUG)
        mlog.setLevel(logging.DEBUG)
        log.debug('Logging level set to DEBUG')


def check_args(parser, args):
    '''
    Check for basic needed arguments; print help if no arguments made, supply
        a message and quit if args not made, or return None if everything is OK
    '''
    # If program run with no arguments
    if not args.api_key and not args.command:
        # Provide the help output
        parser.print_help()
        sys.exit()
    if not args.api_key:
        console('API Key required, use --api_key or -k to supply it')
        sys.exit()
    if not args.command:
        console('Please supply a command, like \'showorgs\'')
        sys.exit()
    return None


def main():
    '''
    Main program function called for execution by the console script
    '''
    parser = argparse.ArgumentParser(
        description='Meraki CLI - A Simple CLI Helper Tool for Meraki Systems',
        formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(help='System control subcommand',
                                       dest='command')
    #######################################################################
    #######################################################################
    # showorgs
    showorgs_parser = subparsers.add_parser(
        'showorgs',
        help='Show Organizations')
    #######################################################################
    #######################################################################
    # showdevices
    showdevices_parser = subparsers.add_parser(
        'showdevices',
        help='Show Devices')
    showdevices_parser.add_argument(
        '-o', '--org_id',
        help='Organization ID',
        metavar='ID',
        required=True,
        dest='org_id')
    #######################################################################
    #######################################################################
    # switchport
    updateswitchport_parser = subparsers.add_parser(
        'updateswitchport',
        help='Update Switch Port')
    showswitchports_parser = subparsers.add_parser(
        'showswitchports',
        help='Show Switch Ports')
    for swparser in [updateswitchport_parser, showswitchports_parser]:
        swparser.add_argument(
            '-s', '--switch_serial',
            help='Switch Serial Number',
            metavar='WORD',
            required=True,
            dest='switch_serial')
    updateswitchport_parser.add_argument(
        '-p', '--port_name',
        help='Port Name',
        metavar='WORD',
        required=True,
        dest='port_name')
    showswitchports_parser.add_argument(
        '-p', '--port_name',
        help='Port Name',
        metavar='WORD',
        required=False,
        dest='port_name')
    updateswitchport_parser.add_argument(
        'attributes',
        help='New Attributes',
        metavar='ATTRIBUTES',
        nargs='*')
    showswitchports_parser.add_argument(
        '-a', "--status",
        help="Interface status instead of configuration",
        dest="status",
        action='store_true')
    #######################################################################
    #######################################################################
    # Basic arguments
    parser.add_argument(
        '-k', '--api_key',
        help='Meraki API Access Key',
        metavar='KEY',
        required=False,
        dest='api_key')
    parser.add_argument(
        '-t', "--table",
        help="Print output as table instead of JSON",
        dest="table",
        action='store_true')
    parser.add_argument(
                        '-d', "--debug",
                        help="""Set debug level (WARNING by default)
    Debug level INFO:  '-d'
    Debug level DEBUG: '-dd'""",
                        dest="debug",
                        action='count')
    parser.add_argument(
                        '-v', '--version',
                        action='version',
                        version=f'Meraki-CLI v{__version__.version}')
    args = parser.parse_args()
    check_args(parser, args)  # Pre-process args
    set_debug_level(args)  # Adjust logging level according to args
    api = get_api(args)  # Auth to Meraki dashboard and get api obj
    # Run function matching the command in the arguments
    globals()[args.command](args, api)
