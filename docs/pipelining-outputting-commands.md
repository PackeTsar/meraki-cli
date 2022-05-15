---
title: Outputting Commands
---

If you want to test out the power of pipelining, but don't necessarily want to have the commands executed automatically (in case you did something wrong), you can use the `-o` switch to output templatized commands instead.

Using the `-o` switch in the receiving command will prevent actual execution, and instead will structure and display commands which will perform that execution; complete with arguments and values.

The scary command from the [Translations](/pipelining-translations) section can be safely tested by adding the `-o` switch:

```
meraki appliance getNetworkApplianceVlans --networkId N_12345 | meraki -o -t "vlanId=id" appliance deleteNetworkApplianceVlan
```

When executed, the output looks like this:

```
~$
~$ meraki appliance getNetworkApplianceVlans --networkId N_12345 | meraki -o -t "vlanId=id" appliance deleteNetworkApplianceVlan

meraki appliance deleteNetworkApplianceVlan --networkId 'N_12345' --vlanId '1'

meraki appliance deleteNetworkApplianceVlan --networkId 'N_12345' --vlanId '200'

meraki appliance deleteNetworkApplianceVlan --networkId 'N_12345' --vlanId '300'

~$
~$
```

You can then copy the output commands one by one to perform their functions manually.
