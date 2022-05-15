---
title: Filtering
---

When multiple items are returned from your command, you can filter them by providing a column name (key) and a regular expression to use to match the item's columns value.

For example, you can return only enabled switch ports on a switch with:

```
meraki -f "enabled:True" switch getDeviceSwitchPortsStatuses --serial 1234-ABCD-5678
```

Since the filtering system honors regular expressions on the pattern side of the `key:pattern` filter statement, you can use something like the below to list out any ports with "user" in their name

```
meraki -f "name:.*user.*" switch getDeviceSwitchPorts --serial 1234-ABCD-5678
```


## AND/OR Logic

The filter (`-f`) argument is reusable and you can use it multiple times to match based on more than one column. By default the filter uses "**OR**" logic when dealing with multiple filters.

For example, the below command will show any enabled ports (regardless of VLAN) and it will also show any ports in VLAN 1000 (regardless of them being enabled or disabled).

```
meraki -f "enabled:True" -f "vlan:1000" switch getDeviceSwitchPorts --serial 1234-ABCD-5678
```

If you want to combine those filters so displayed items have to match both of them. Pass in the `-a` switch to change the filter logic to "**AND**" like:

`meraki -f "enabled:True" -f "vlan:1000" -a switch getDeviceSwitchPorts --serial 1234-ABCD-5678`
