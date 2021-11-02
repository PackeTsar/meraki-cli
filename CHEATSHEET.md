###  [< (Back) to Meraki-CLI Home](https://github.com/PackeTsar/meraki-cli/)


# Meraki-CLI Command Cheat Sheet

Below are some example commands and command-combinations I've found particularly useful to get things done quickly and effeciently. If you have a useful command you'd like to share please [open an issue](https://github.com/PackeTsar/meraki-cli/issues/new) to share it or submit a merge-request to the repo.

Placeholders in the command examples will use the format `<placeholder>`


# Table of Contents
- [List Organizations](#list-organizations)
- [List Networks in an Organization](#list-networks-in-an-organization)
- [List Device Inventory of an Organization](#list-device-inventory-of-an-organization)
- [List Assigned Devices in an Organization](#list-assigned-devices-in-an-organization)
- [List Unassigned Devices in an Organization](#list-unassigned-devices-in-an-organization)
- [List All Switches in an Organization](#list-all-switches-in-an-organization)
- [List Devices in a Network](#list-devices-in-a-network)
- [Claim a Device into a Network](#claim-a-device-into-a-network)
- [Change Device Name](#change-device-name)
- [Change Device Name (Partial Serial)](#change-device-name--partial-serial-)
- [List Port Settings on a Switch](#list-port-settings-on-a-switch)
- [Set the Name of a Switch Port](#set-the-name-of-a-switch-port)
- [Set a Switch Port to Access a VLAN](#set-a-switch-port-to-access-a-vlan)
- [List SVIs on a Switch](#list-svis-on-a-switch)
- [Create a SVI on a Layer-3 Switch](#create-a-svi-on-a-layer-3-switch)
- [Create a SVI and Add it to OSPF on a Layer-3 Switch](#create-a-svi-and-add-it-to-ospf-on-a-layer-3-switch)
- [Set DHCP Settings on SVI (Using the SVI Name)](#set-dhcp-settings-on-svi--using-the-svi-name-)
- [Filter ports on a switch using LLDP info](#filter-ports-on-a-switch-using-lldp-info)
- [Set camera ports to specific VLAN](#set-camera-ports-to-specific-vlan)


# Cheat Sheet


## List Organizations

Print a list of organizations (and their organization ID numbers) to which you have access.

```
meraki organizations getOrganizations
```


## List Networks in an Organization

Print a list of networks (and their network ID numbers) within an organization

```
meraki organizations getOrganizationNetworks --organizationId <organizationId>
```


## List Device Inventory of an Organization

Print a list of devices in the inventory of a network

```
meraki organizations getOrganizationInventoryDevices --organizationId <organizationId>
```


## List Assigned Devices in an Organization

Print a list of devices in an organization which are currently assigned to a network

```
meraki -f networkId:N_ organizations getOrganizationInventoryDevices --organizationId <organizationId>
```


## List Unassigned Devices in an Organization

Print a list of devices in an organization which are currently not assigned to a network

```
meraki -f networkId:None organizations getOrganizationInventoryDevices --organizationId <organizationId>
```


## List All Switches in an Organization

Print a list of all switches in an organization

```
meraki -f model:^MS organizations getOrganizationInventoryDevices --organizationId <organizationId>
```


## List Devices in a Network

Print a list of devices assigned to a particular network.

```
meraki networks getNetworkDevices --networkId <networkId>
```


## List All Switch Stacks in a Network

Print a list of all switch stacks within a particular network.

```
meraki switch getNetworkSwitchStacks --networkId <networkId>
```


## Claim a Device into a Network

Claim an unassigned device into an existing Meraki Network

```
meraki networks claimNetworkDevices --networkId <networkId> --serials <serials>
```


## Change Device Name

Change the name of a device using the serial number of the device

```
meraki devices updateDevice --serial <serial> --name <name>
```


## Change Device Name (Partial Serial)

Change the name of a device in your organization using a partial serial number.

> NOTE: If multiple serials match the filter criterion, then you will end up changing the name of multiple devices.

```
meraki -f serial:<partial_serial> organizations getOrganizationInventoryDevices --organizationId <organizationId> | meraki devices updateDevice --name <name>
```


## List Port Settings on a Switch

Print out ports and their settings for a particular switch

```
meraki switch getDeviceSwitchPorts --serial <serial>
```


## Set the Name of a Switch Port

Set the name (description) of a port on a switch

```
meraki switch updateDeviceSwitchPort --serial <serial> --portId <portId> --name "<name_or_description>"
```


## Set a Switch Port to Access a VLAN

Change a switch port settings to make it an "access" port and set a VLAN ID for it

```
meraki switch updateDeviceSwitchPort --serial <serial> --type access --portId <portId> --vlan <vlan>
```


## List SVIs on a Switch

Print a list of SVIs on a layer-3 switch

```
meraki switch getDeviceSwitchRoutingInterfaces --serial <serial>
```


## Create a SVI on a Layer-3 Switch

Create a new SVI (switched virtual interface) on a layer-3 switch

> NOTE: The first SVI created on a switch requires the `defaultGateway` parameter be included.

```
meraki switch createDeviceSwitchRoutingInterface --serial <serial> --name <name> --vlanId <vlanId> --subnet "<subnet>" --interfaceIp <interfaceIp> --defaultGateway <defaultGateway>
```


## Create a SVI and Add it to OSPF on a Layer-3 Switch

Create a new SVI on a layer-3 switch and add that SVI to OSPF in a passive state.

> NOTE: OSPF settings shown are an example and should be adjusted to your needs.

```
meraki switch createDeviceSwitchRoutingInterface --serial <serial> --name <name> --vlanId <vlanId> --subnet "<subnet>" --interfaceIp <interfaceIp> --ospfSettings '{"area": 0, "cost": 1, "isPassiveEnabled": true}'
```


## Set DHCP Settings on SVI (Using the SVI Name)

Set DHCP relay on a layer-3 switch SVI (which typically requires the SVI ID number) using the name of the SVI instead of the ID number

```
meraki -f name:<svi_name> switch getDeviceSwitchRoutingInterfaces --serial <serial> | meraki -j switch updateDeviceSwitchRoutingInterfaceDhcp --serial <serial> --dhcpMode dhcpRelay --dhcpRelayServerIps '["<ip_address>"]'
```


## Filter ports on a switch using LLDP info

List only switch ports with Meraki cameras connected to them

```
meraki -f "lldp:Meraki MV" switch getDeviceSwitchPortsStatuses --serial <serial>
```

List only switch ports with Meraki access points connected to them

```
meraki -f "lldp:Meraki MR" switch getDeviceSwitchPortsStatuses --serial <serial>
```

List only switch ports with Meraki switches connected to them

```
meraki -f "lldp:Meraki MR" switch getDeviceSwitchPortsStatuses --serial <serial>
```


## Set camera ports to specific VLAN

Set all ports on a switch with Meraki cameras connected to access a specific VLAN

```
meraki -f "lldp:Meraki MV" switch getDeviceSwitchPortsStatuses --serial <serial> | meraki switch updateDeviceSwitchPort --serial <serial> --vlan <vlan>
```
