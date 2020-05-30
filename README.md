# Meraki-CLI

[![Build Status](https://travis-ci.org/PackeTsar/meraki-cli.svg?branch=master)](https://travis-ci.org/PackeTsar/meraki-cli)
[![PyPI](https://img.shields.io/pypi/v/meraki-cli.svg)](https://pypi.python.org/pypi/meraki-cli)
[![Python Versions](https://img.shields.io/pypi/pyversions/meraki-cli.svg)](https://pypi.python.org/pypi/meraki-cli)

A Simple CLI Helper Tool for Meraki Systems

Quick Install: `pip install meraki-cli`


-----------------------------------------
##   VERSION   ##
The version of Meraki-CLI documented here is: **0.1.2**


-----------------------------------------
##   GETTING STARTED   ##

## Prepare your OS

In order to use Meraki-CLI, you need to have Python 3 installed on your OS. If you do not yet have Python 3 installed, visit [https://github.com/PackeTsar/Install-Python](https://github.com/PackeTsar/Install-Python)


### Getting and Using your API Key

Meraki-CLI is command-line driven and once installed can be run with the command `mcli`

Once you have installed Meraki-CLI, you can see the command guide with `mcli -h`.

In order to operate Meraki-CLI you need to input your Meraki API key using the `-k` argument.
- You can obtain a Meraki API key by logging into the Meraki dashboard and clicking your user name in the top right corner and browsing to **My profile** then view the 'API Access' section near the bottom of the page
- Click on the 'Generate new API key' button and copy down your new API key before saving. It will be a long hexadecimal string.

The Meraki-CLI tool accepts a few general arguments (like `-k`, `-t`, and `-d`) and then accepts a command (like `showorgs` and `showdevices` which often have their own arguments they require). The general arguments like the API key argument (`-k`) must be input before the command. Only the command-specific arguments can be made after the command.


### A Few Starting Commands

Once you have your new key, try printing out you list organizations with the command `mcli -k API_KEY_HERE showorgs`, substituting in your API key. This will print out a formatted JSON list of your organizations.

You can reformat this data into a table by adding the `-t` switch (before the command) to look something like `mcli -t -k API_KEY_HERE showorgs`
- It is important to note that the columns included in a table often do not include all of the data returned from the API. If you need to see all the data returned, then remove the `-t` switch and allow the tool to print out JSON data.

To see the general help menu, enter a `-h` argument in before the command (like `mcli -h`). To see a command's specific help menu, enter the `-h` after the command (like `mcli updateswitchport -h`)

You can take one of the organization ID's from your `showorgs` and list out (in a table) all the devices for that organization with the command `mcli -t -k API_KEY_HERE showdevices -o ORG_ID_HERE`

If you have any Meraki MS switches available, try viewing the port configurations with `mcli -t -k API_KEY_HERE showswitchports -s SERIAL_NUMBER_HERE` or you can view the operational port stats by appending the `-a` switch to the command like `mcli -t -k API_KEY_HERE showswitchports -s SERIAL_NUMBER_HERE -a`


### Making Some Changes

Pushing changes into Meraki is done by providing positional (no `-x` prefixing the value) key/value arguments after the command. These key value arguments must match key/value attributes you see in JSON. You can provide as many of these key-value arguments as you want in a single command. For example, we can change the VLAN assigned to a port to VLAN 100 with the command:
  - `mcli -k API_KEY_HERE updateswitchport -s SERIAL_NUMBER_HERE -p PORT_NUMBER_HERE vlan:100`

We can add to this by providing more attributes to update on the port, like:
  - `mcli -k API_KEY_HERE updateswitchport -s SERIAL_NUMBER_HERE -p PORT_NUMBER_HERE vlan:100 enabled:true name:Special_Port`

If any of your attribute arguments requires spaces or special characters, make sure to wrap that argument in quotes like:
  - `mcli -k API_KEY_HERE updateswitchport -s SERIAL_NUMBER_HERE -p PORT_NUMBER_HERE 'name:Supervisors Desk Port`


-----------------------------------------
##   CONTRIBUTING   ##

This project is very new and has been created out of need. As you may see it is currently very limited in what it can do, but has been built to be easy to extend and add features. If you have a feature you would like to see built into it, please open up an issue in Github and describe your desired feature. Any accepted feature requests will be listed in the [Enhancement Requests and Known Bugs](https://github.com/PackeTsar/meraki-cli/issues/1) issue page.

If you find a need for a feature and you add it in yourself, or you fix a bug you found, please feel free to open up a merge request!
