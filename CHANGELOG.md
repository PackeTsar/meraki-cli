###  [< (Back) to Meraki-CLI Home](https://github.com/PackeTsar/meraki-cli/)


# Meraki-CLI Version Change Log

Documented below is a history of Meraki-CLI versions and a log of changes to each version


# Table of Contents
- [v1.0.5 -> v1.0.6](#v106)
- [v1.0.6 -> v1.1.0](#v110)
- [v1.1.0 -> v1.2.0](#v120)


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

## v1.2.0

### New Features

- **Optional Arguments instead of --kwargs**
    - Previous versions of Meraki-CLI required you to provide optional arguments at the command line as JSON-parsable data using the `--kwargs` argument. This would look something like `meraki appliance createNetworkApplianceVlan --networkId N_12345 --id 100 --name "My New VLAN" --kwargs '{"applianceIp": "10.0.0.1", "subnet": "10.0.0.0/24"}'`
        - On Windows it would have to look like `meraki appliance createNetworkApplianceVlan --networkId N_12345 --id 100 --name "My New VLAN" --kwargs "{""applianceIp"": ""10.0.0.1"", ""subnet"": ""10.0.0.0/24""}"`
    - This `--kwargs` format is difficult to use and prone to error
    - The new functionality will read through Optional Arguments provided by the user at the CLI and will parse them appropriately. This allows a simpler command to be used instead: `meraki appliance createNetworkApplianceVlan --networkId N_12345 --id 100 --name "My New VLAN" --applianceIp "10.0.0.1" --subnet "10.0.0.0/24"` where the `--applianceIp` and `--subnet` arguments are broken out on their own; removing the need for the curly-braces, formatting, and double-double quotes on Windows platforms
    - The `--kwargs` argument still exists for more advanced usage, but its focus has been greatly reduced in the documentation in lieu of using the new optional arguments like `--applianceIp` and `--subnet`

### Bug Fixes

- **Changed config file name and searched locations**
    - ISSUE: The config file feature released in v1.1.0 used `meraki` directory names and the `meraki.conf` filename for config files. This might conflict with official Meraki directory and file names in the future and needed to be changed to something unlikely to conflict.
    - FIXES: The directories now use the name `meraki-cli` and the standard config filename is `meraki-cli.conf`. The searched parent directories remain the same as in v1.1.0.

- **Removed Meraki SDK version lock**
    - ISSUE: The Official Meraki SDK which existed at the time of the release of Meraki-CLI v1.1.0 had a major bug which prevented it from being usable. To prevent users from installing it and being unable to use Meraki-CLI, a version lock was imposed on the dependency; forcing installation of v1.4.3 of the official Meraki SDK.
    - FIXES: Meraki has since fixed these issues and the version lock has been lifted.
