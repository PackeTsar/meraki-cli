---
title: Pipelining
---

# Pipelining

Being able to manipulate the Meraki dashboard from the CLI can be quite useful, but its power grows exponentially when you are able to use pipelining.

Pipelining allows you to pass the Meraki objects returned in one command into another and do something with them.

!!! note "Store Your API Key"
    When using pipelining, you will likely want to store your API key as an environment variable or in a config file since it will need to be available to each instance of the program.

    Otherwise you would have to insert it multiple times like `meraki -k abcd1234 <commands> | meraki -k abcd1234 <commands>`.

A simple example of pipelining is to display the switch port statuses of the ports on all switches in a network. To do this use:

```
meraki networks getNetworkDevices --networkId N_12345 | meraki switch getDeviceSwitchPorts
```

The above command can be interpreted the following way:

1. The first command (the `getNetworkDevices` command before the pipe) is retrieving and returning all network device objects in a network. Each device object will have a `serial` number attribute contained in it

2. The pipe between the commands is sending the output of the first command into the input of the second

3. The second command (the `getDeviceSwitchPorts` command) is taking each object (switch) in its input and retrieving that object's switch ports

!!! abstract "Attributes Turn Into Arguments"
    Since the only argument required by the `getDeviceSwitchPorts` command is `--serial`, and the `serial` attribute is contained in each object coming from the first command, the second is able to use that information to loop through the input objects and execute the command on them.

This pipelining functionality should be recognizable to anybody familiar with common pipelining in Linux or PowerShell.

## Add Some Filtering

If you wanted to, for example, filter the output of the first command to only return MS250 model switches, you can use a filter in it like:

```
meraki -f 'model:MS250' networks getNetworkDevices --networkId N_12345 | meraki switch getDeviceSwitchPorts
```

This would loop through all the switches in the network and return all the port configs, but only on MS250 switches.
