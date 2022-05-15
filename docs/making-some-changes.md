---
title: Making Some Changes
---

Pushing changes into Meraki is done by running the correct command and passing in the necessary arguments.

## Update Device

For example, to rename a device, we just run the `devices updateDevice` command with the proper arguments included:

```
~$
~$ meraki devices updateDevice --serial Q2HP-F5K5-R88R --name NEW_DEVICE_NAME
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ lat              ┃ lng               ┃ address ┃ serial         ┃ mac               ┃ lanIp         ┃ url              ┃ networkId            ┃ name            ┃ model    ┃ switchProfileId ┃ firmware       ┃ floorPlanId ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 37.4180951010362 │ -122.098531723022 │         │ Q2HP-F5K5-R88R │ 88:15:44:df:f3:af │ 10.10.10.131  │ https://n149.me… │ L_646829496481105433 │ NEW_DEVICE_NAME │ MS220-8P │ None            │ switch-11-31   │ None        │
└──────────────────┴───────────────────┴─────────┴────────────────┴───────────────────┴───────────────┴──────────────────┴──────────────────────┴─────────────────┴──────────┴─────────────────┴────────────────┴─────────────┘
~$
~$
```

## Update Device Switch Port

Or if we want to change the VLAN ID and name of a MS switch port, we can use:

```
meraki switch updateDeviceSwitchPort --serial 1234-ABCD-5678 --portId 1 --vlan 100 --name "Data Port"
```

If the change succeeds, you will often see the newly updated item echoed back like this:

```
~$
~$ meraki switch updateDeviceSwitchPort --serial Q2HP-F5K5-R88R --portId 1 --vlan 100 --name "Data Port"
┏━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━┳━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ portId ┃ name      ┃ enabled ┃ poeEnabled ┃ type  ┃ vlan ┃ voiceVlan ┃ allowedVlans ┃ isolationEnabled ┃ rstpEnabled ┃ stpGuard ┃ linkNegotiation ┃ portScheduleId ┃ udld       ┃
┡━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━╇━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 1      │ Data Port │ True    │ True       │ trunk │ 100  │ None      │ all          │ False            │ True        │ disabled │ Auto negotiate  │ None           │ Alert only │
└────────┴───────────┴─────────┴────────────┴───────┴──────┴───────────┴──────────────┴──────────────────┴─────────────┴──────────┴─────────────────┴────────────────┴────────────┘
~$
~$
```

## Update Device Switch Port (Help Page)

Many commands which make changes to the dashboard (like `updateDeviceSwitchPort` above) have optional arguments (like `--vlan` and `--name`) which are used to send those changes. See the below help page for the `updateDeviceSwitchPort` command:

```
~$
~$ meraki switch updateDeviceSwitchPort -h
usage: meraki-cli.py switch updateDeviceSwitchPort [-h] --serial STRING --portId STRING [--kwargs JSON_STRING]

UPDATE A SWITCH PORT

https://developer.cisco.com/meraki/api-v1/#!update-device-switch-port

All Arguments:
  --serial (string): (required)
  --portId (string): (required)
  --name (string): The name of the switch port
  --tags (array): The list of tags of the switch port
  --enabled (boolean): The status of the switch port
  --type (string): The type of the switch port ('trunk' or 'access')
  --vlan (integer): The VLAN of the switch port. A null value will clear the value set for trunk ports.
  --voiceVlan (integer): The voice VLAN of the switch port. Only applicable to access ports.
  --allowedVlans (string): The VLANs allowed on the switch port. Only applicable to trunk ports.
  --poeEnabled (boolean): The PoE status of the switch port
  --isolationEnabled (boolean): The isolation status of the switch port
  --rstpEnabled (boolean): The rapid spanning tree protocol status
  --stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard')
  --linkNegotiation (string): The link speed for the switch port
  --portScheduleId (string): The ID of the port schedule. A value of null will clear the port schedule.
  --udld (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
  --accessPolicyType (string): The type of the access policy of the switch port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'
  --accessPolicyNumber (integer): The number of a custom access policy to configure on the switch port. Only applicable when 'accessPolicyType' is 'Custom access policy'
  --macAllowList (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'
  --stickyMacAllowList (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'
  --stickyMacAllowListLimit (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'
  --stormControlEnabled (boolean): The storm control status of the switch port
  --flexibleStackingEnabled (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.

Function Signature:
  >>> def updateDeviceSwitchPort(serial: str, portId: str, **kwargs):

Required Arguments:
  --serial STRING       (required)
  --portId STRING       (required)

Misc Arguments:
  -h, --help            Show help for this command
  --kwargs JSON_STRING  (Advanced Users) Optional arguments in JSON format
~$
~$
```

## Providing Arguments

For the `updateDeviceSwitchPort` command, you can see from the help page above that there are two required arguments: `--serial` and `--portId`. There are also many optional arguments like `--name`, `--tags`, `--enabled`, `--vlan`, etc. Each of the arguments has its value type listed in the help page.

Simple value types like string, integer, and boolean are pretty straightforward. The can be provided like:

- `--name "Some Descriptive Name"` (string)
- `--vlan 100` (integer)
- `--enabled true` (boolean)

---

Once you're familiar with providing simple arguments to Meraki-CLI like the examples above, you may want to review how to provide [Complex Argument Values](../complex-argument-values/)

[Next: Complex Argument Values :octicons-arrow-right-24:](../complex-argument-values/){ .md-button .md-button--primary }
