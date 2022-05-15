---
title: Overriding Values
---

# Pipelining: **Overriding Values**

Sometimes you want to use the output of one command to feed another, but you want to change something in the data before submitting it in that second command.

You can do this by providing the changed argument in the command line of the second argument. For example:

```
meraki appliance getNetworkApplianceVlans --networkId N_11111 | meraki appliance createNetworkApplianceVlan --networkId N_22222
```

Here, you are taking all of the configured appliance VLANs in network **N_11111** and are pushing them into the `createNetworkApplianceVlan` to create new appliance VLANs.

But first you are overriding the `--networkId` attribute of those VLAN objects so they are applied to a different network: the **N_22222** network.

In effect, you are copying all appliance VLANs from one network to another.
