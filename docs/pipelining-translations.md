---
title: Translations
---

# Pipelining: **Translations**

At times the attribute names of objects returned from one command do not exactly match the required input names of another, even though the actual data is the same.

For example: the output of the `getNetworkApplianceVlans` command assigns VLAN ID numbers to the attribute name `id`, however the `deleteNetworkApplianceVlan` command requires the argument name `vlanId`.

To deal with this we have to provide a translation using the `-t` argument.

If you wanted to delete all the appliance VLANs configured on a network, you would need to provide a translation on the second instance like below.

!!! danger "Don't Run This Command"
    The below command is instructing Meraki-CLI to delete all MX firewall VLAN interfaces configured on a particular network. It is provided as an example of a use case.

    Don't run it unless that is explicitly what you are trying to do.

```
meraki appliance getNetworkApplianceVlans --networkId N_12345 | meraki -t "vlanId=id" appliance deleteNetworkApplianceVlan
```

The `-t "vlanId=id"` argument is effectively telling the receiving program to use the `id` attributes of its input to fill the `vlanId` argument required by the `deleteNetworkApplianceVlan` command.
