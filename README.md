# Meraki-CLI

[![Build Status](https://travis-ci.com/PackeTsar/meraki-cli.svg?branch=master)](https://travis-ci.com/PackeTsar/meraki-cli)
[![PyPI](https://img.shields.io/pypi/v/meraki-cli.svg)](https://pypi.python.org/pypi/meraki-cli)
[![Python Versions](https://img.shields.io/pypi/pyversions/meraki-cli.svg)](https://pypi.python.org/pypi/meraki-cli)

A Simple CLI tool to automate and control your Meraki Dashboard!

Quick Install: `pip install meraki-cli`


-----------------------------------------
## VERSION
The version of Meraki-CLI documented here is: **0.3.0**


-----------------------------------------
## ABOUT
Meraki-CLI is a wrapper around the [Meraki Python Dashboard API SDK](https://github.com/meraki/dashboard-api-python). It takes all published functions in the library and makes them available to the user as a standard command-line tool with `-h` help options, commands, switches, and arguments. It also supports classic Linux-style pipelining, allowing the output of one instance of the program to be piped to the input of another.

### Examples

- List your associated organizations: `meraki organizations getOrganizations`
- List the Meraki networks within an organization: `meraki organizations getOrganizationNetworks --organizationId 123456`
- List the MX VLANs on a network: `meraki appliance getNetworkApplianceVlans --networkId N_12345`
- Add a new MX VLAN to a network: `meraki appliance createNetworkApplianceVlan --networkId 'N_12345' --id '100' --name 'My New VLAN' --kwargs '{"applianceIp": "10.0.0.1", "subnet": "10.0.0.0/24"}'`


-----------------------------------------
## TABLE OF CONTENTS
1. [Getting Started](#getting-started)
    - [Prepare your OS](#prepare-your-os)
    - [Getting and Using your API Key](#getting-and-using-your-api-key)
    - [A Few Starting Commands](#a-few-starting-commands)
    - [Making Some Changes](#making-some-changes)
    - [Debugging and Logging](#debugging-and-logging)
    - [Filtering](#filtering)
2. [PIPELINING](#pipelining)
    - [Overriding Values](#overriding-values)
    - [Translations](#translations)
    - [Outputting Commands](#outputting-commands)
3. [CONTRIBUTING](#contributing)


-----------------------------------------
## GETTING STARTED

## Prepare your OS

In order to use Meraki-CLI, you need to have Python 3 installed on your OS. If you do not yet have Python 3 installed, visit [https://github.com/PackeTsar/Install-Python](https://github.com/PackeTsar/Install-Python). If you are installing on Windows, make sure to


## Install Meraki-CLI

The easiest (and recommended) way to install Meraki-CLI is to use PIP. You can use PIP to install Meraki-CLI with the command `pip3 install meraki-cli` or `python3 -m pip install meraki-cli`. To see if Meraki-CLI was successfully installed, run the `meraki` command and see if it displays the help menu.


## Getting and Using your API Key

Meraki-CLI is command-line driven and once installed can be run with the command `meraki`. Once you have installed Meraki-CLI, you can see the command guide by running the command by itself.

In order to operate Meraki-CLI you need to input your Meraki API key using one of two methods:

1. Saving your API key as an environment variable using `export MERAKI_DASHBOARD_API_KEY=12345`
   - Once saved as an environment variable, you don't need to use the `-k` option when running commands
2. Use the `-k 12345` or `--apiKey 12345` argument at the top level of the command like `meraki -k 12345`

You can obtain a Meraki API key by logging into the Meraki dashboard and clicking your user name in the top right corner and browsing to **My profile** then view the 'API Access' section near the bottom of the page. Then click on the '**Generate new API key**' button and copy down your new API key before saving. It will be a long hexadecimal string.


## A Few Starting Commands

Once you have your new key, try printing out you list organizations with the command `meraki -k API_KEY_HERE organizations getOrganizations`, substituting in your API key. This will print out a formatted table of your organizations.

Take one of your organization ID numbers and look at the networks in it with `meraki organizations getOrganizationNetworks --organizationId 123456`

You can reformat any of this data into JSON output by adding the `-j` switch (before the command) to look something like `meraki -j organizations getOrganizations`
- It is important to note that the columns included in a table often do not include all of the data returned from the API. If you need to see all the data returned, then use the `-j` switch and allow the tool to print out JSON data.

You can also change the table data which is output by filtering and ordering table columns. To do this, use the `-c` argument and provide a comma-seperated list of columns to display. Example: `meraki -c id,name,description`

To see any help menu, use the `-h` option at any command level:
- `meraki -h` or just `meraki` will show you the top level options and arguments
- `meraki appliance -h` or just `meraki appliance` will show you all the appliance-related commands
- `meraki appliance createNetworkApplianceVlan -h` will show you an instruction page with all the arguments and options available for creating a new network appliance VLAN


If you have any Meraki MS switches available, try viewing the port configurations with `meraki switch getDeviceSwitchPorts --serial 1234-ABCD-5678` or you can view the operational port stats by using `meraki switch getDeviceSwitchPortsStatuses --serial 1234-ABCD-5678`


## Making Some Changes

Pushing changes into Meraki is done by running the correct command and passing in the required arguments. At times, this requires passing JSON data into the CLI with something like `--kwargs '{"applianceIp": "10.0.0.1", "subnet": "10.0.0.0/24"}'`. Any data you need to pass into the program which is not a defined argument when viewing the help page with `-h` has to be passed in this way. The help page for a specific command will often give you details about what kinds of data can be passed in this way.

For example, if we want to change the VLAN ID on a MS switch port, we would use:

`meraki switch updateDeviceSwitchPort --serial 1234-ABCD-5678 --portId 24 --kwargs '{"vlan": "100"}'`


## Debugging and Logging

If you are having trouble figuring out why something is not working, you set the debugging level to one of four levels
- Level 0 (default): Only warnings and errors will be displayed or logged
- Level 1 (`-d`): General status and program progress will be reported
- Level 2 (`-dd`): General program progress as well as Meraki API library debugging will be reported
- Level 3 (`-ddd`): Program progress, Meraki API library debugging, and full data dumps will be reported

If you want to stow those logs away, you can define a log file using something like `-l logs.txt`. Only logs printed to the screen will be written to the file, so you also need to enable a debugging level.


## Filtering

When multiple items are returned from your command, you can filter them by providing a column name (key) and a regular expression to use to match the item's columns value.

For example, you can view only enabled switch ports on a switch with:

`meraki -f "enabled:True" switch getDeviceSwitchPortsStatuses --serial 1234-ABCD-5678`

The filter (`-f`) argument is reusable and you can use it multiple times to match based on more than one column. By default the filter uses "OR" logic when dealing with multiple filters. For example, the below command will show any enabled ports and any ports in VLAN 1000.

`meraki -f "enabled:True" -f "vlan:1000" switch getDeviceSwitchPorts --serial 1234-ABCD-5678`

If you want to combine those filters so displayed items have to match both of them. Pass in the `-a` switch to change the filter logic to "AND" like:

`meraki -f "enabled:True" -f "vlan:1000" -a switch getDeviceSwitchPorts --serial 1234-ABCD-5678`


-----------------------------------------
## PIPELINING

Being able to manipulate the Meraki dashboard from the CLI can be quite useful, but its power grows exponentially when you are able to use pipelining. Pipelining allows you to pass the Meraki objects returned in one command into another and do something with them.

A simple example of this is to display the switch port statuses of the ports on all switches in a network. To do this use:

`meraki networks getNetworkDevices --networkId N_12345 | meraki switch getDeviceSwitchPorts`

The above command can be interpreted the following way:
- The first command (before the pipe) is retrieving and returning all network device objects in a network. Each device object will have a `serial` number attribute with it.
- The pipe between the commands is sending the output of the first command into the input of the second.
- The second command is taking each object in its input and retrieving that object's switch ports. Since the only argument required by the `getDeviceSwitchPorts` command is `--serial`, and the `serial` attribute is contained in each object coming from the first command, the second is able to use that information to loop through the input objects and execute the command on them.
- This functionality should be recognizable to anybody familiar with common pipelining in Linux or PowerShell.

If you, for example, wanted to filter the output of the first command to only output MS250 model switches, you can use a filter in it like:

`meraki -f 'model:MS250' networks getNetworkDevices --networkId N_12345 | meraki switch getDeviceSwitchPorts`


### Overriding Values

Sometimes you want to use the output of one command to feed another, but you want to change something in the data before submitting it in that second command. You can do this by simply providing the changed argument in the command line of the second argument. For example:

`meraki appliance getNetworkApplianceVlans --networkId N_11111 | meraki appliance createNetworkApplianceVlan --networkId N_22222`

Here you are taking all of the configured appliance VLANs in network N_11111 and are pushing them into the `createNetworkApplianceVlan` to create new appliance VLANs. But first you are overriding the `--networkId` attribute of those VLAN objects so they are applied to a different network. You are effectively copying all appliance VLANs from one network to another.


### Translations

At times the attribute names of objects output from one command do not exactly match the required input names of another, even though the actual data is the same. For example: the output of the `getNetworkApplianceVlans` command assigns VLAN ID numbers to the attribute name `id`, however the `deleteNetworkApplianceVlan` command requires the argument name `vlanId`. To deal with this we have to provide a translation using the `-t` argument. If you wanted to delete all the appliance VLANs configured on a network **NOT ADVISABLE**, you would need to provide a translation on the second instance like:

`meraki appliance getNetworkApplianceVlans --networkId N_12345 | meraki -t "vlanId=id" appliance deleteNetworkApplianceVlan`

The `-t "vlanId=id"` argument is effectively telling the receiving program to use the `id` attributes of its input to fill the `vlanId` argument required by the `deleteNetworkApplianceVlan` command.


### Outputting Commands

If you want to test out the power of pipelining, but don't necessarily want to have the commands executed automatically (in case you did something wrong), you can use the `-o` switch to output templatized commands instead. Using the `-o` switch in the receiving command will prevent actual execution, and instead will structure and display commands which will perform that execution; complete with arguments and values. The above command can be safely tested using the below:

`meraki appliance getNetworkApplianceVlans --networkId N_12345 | meraki -o -t "vlanId=id" appliance deleteNetworkApplianceVlan`


-----------------------------------------
## CONTRIBUTING

This project is very new and has been created out of need. As you may see it is currently very limited in what it can do, but has been built to be easy to extend and add features. If you have a feature you would like to see built into it, please open up an issue in Github and describe your desired feature. Any accepted feature requests will be listed in the [Enhancement Requests and Known Bugs](https://github.com/PackeTsar/meraki-cli/issues/1) issue page.

If you find a need for a feature and you add it in yourself, or you fix a bug you found, please feel free to open up a merge request!
