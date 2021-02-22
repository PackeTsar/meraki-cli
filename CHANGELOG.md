###  [< (Back) to Meraki-CLI Home](https://github.com/PackeTsar/meraki-cli/)


# Meraki-CLI Version Change Log

Documented below is a history of Meraki-CLI versions and a log of changes to each version


# Table of Contents
- [v1.0.5 -> v1.0.6](#v106)
- [v1.0.6 -> v1.1.0](#v110)


# Versions

## v1.0.6

### Bug Fixes

- **Cryptic error with malformatted translation**
    - ISSUE: When a poorly formatted translation is entered, the error is not easy to understand. It is a generic Python exception
    - FIXES: 20cfc8c07c7cbd09e1f9c684eb14a33ee2bf4cc7
- **Error Kills Looped Execution**
    - ISSUE: Looped execution (like when pipelining) can be broken by a single error in one of the execution events. This can be seen by issuing `meraki organizations getOrganizations | meraki -t "organizationId=id" organizations getOrganizationNetworks` when at least one of the organizations is not API-enabled. May want to add error catching or control when performing looped execution.
    - FIXES: 800727df6a7cc24d18e0c6ac751714ec2f4498bf

## v1.1.0

### New Features

- **Arguments From File**
    - Meraki-CLI will now read arguments from a static config file by either explicitly directing it with an option like `-c ~/meraki.conf`, or by placing a `meraki.conf` file in one of a few searched locations. More info can be found in the [Using a Config File](https://github.com/PackeTsar/meraki-cli/#using-a-config-file) section in the README.

### Bug Fixes

- **Tabulation problems with nested data**
    - ISSUE: The `getNetworkApplianceFirewallL3FirewallRules` function returns a list of rules nested in a dict like `{"rules": [ruledict1, ruledict2]}` which breaks the tabulated output. Need to parse appropriately.
    - FIXES: Added logic to `_table_ready_dicts` to look over returned data to try to find "tabulatable" data.
