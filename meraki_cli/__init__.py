#!/usr/bin/env python3


'''
Main import file used when 'import meraki_cli'
'''


from . import __version__


name = "meraki_cli"
# HTTP User-Agent header setting for HTTP requests
_user_agent = __version__.user_agent

# Program version
__version__ = __version__.version
