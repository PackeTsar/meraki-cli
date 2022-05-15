---
title: A Few Starting Commands
---

## Get Organizations

Once you have your new key saved, try listing out your organizations with the command:

```
meraki organizations getOrganizations
```

This will print out a formatted table of your organizations.

If you didn't save your API key as an environment variable and also didn't set up a config file, you can include the `-k` argument and  issue:

```
meraki -k API_KEY_HERE organizations getOrganizations
```

!!! info "Omitting the `-k` Argument"
    All following command examples in this section will omit the `-k` argument and will assume you are using an environment variable or a config file.

---

## Get Organization Networks

Take one of your organization ID numbers and look at the networks in it with:

```
meraki organizations getOrganizationNetworks --organizationId 123456
```

You can reformat any of this data into JSON output by adding the `-j` switch (before the command) to look something like:

```
meraki -j organizations getOrganizationNetworks --organizationId 123456
```

---

## Get Device Switch Ports

If you have any Meraki MS switches available, try viewing the port configurations with:

```
meraki switch getDeviceSwitchPorts --serial 1234-ABCD-5678
```

or you can view the operational port stats by using:

```
meraki switch getDeviceSwitchPortsStatuses --serial 1234-ABCD-5678
```

---

## Table Format Manipulations

!!! tip "Incomplete Columns"
    It is important to note that data returned in a table format sometimes does not include all of the data returned from the API.

    This is because some data returned from the API cannot be logically formatted into a table due to its complexity.

    If you need to see all the data returned from the API, then use the `-j` switch and allow the tool to print out the data in JSON format.

You can change the table data which is output by filtering and ordering the table columns. To do this, use the `-s` argument and provide a comma-seperated list of columns to display. Example:

```
meraki -s id,name organizations getOrganizationNetworks --organizationId 123456
```

---

## Command Help

To see any help menu, use the `-h` option at any command level:

- `meraki -h` or just `meraki` will show you the top level options and arguments
- `meraki appliance -h` or just `meraki appliance` will show you all the appliance-related commands
- `meraki appliance createNetworkApplianceVlan -h` or just `meraki appliance createNetworkApplianceVlan` will show you an instruction page with all the arguments and options available for creating a new network appliance VLAN.

You can also view all supported Meraki-CLI commands on the [Meraki-CLI Command Guide](https://github.com/PackeTsar/meraki-cli/blob/master/COMMAND_GUIDE.md){:target="_blank"}

---

Now that you are familiar with running Meraki-CLI commands which show the current configuration or state of the network, we can try [Making Some Changes](../making-some-changes/)

[Next: Making Some Changes :octicons-arrow-right-24:](../making-some-changes/){ .md-button .md-button--primary }
