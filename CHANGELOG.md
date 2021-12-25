###  [< (Back) to Meraki-CLI Home](https://github.com/PackeTsar/meraki-cli/)


# Meraki-CLI Version Change Log

Documented below is a history of Meraki-CLI versions and a log of changes to each version


# Table of Contents
- [v1.0.5 -> v1.0.6](#v106)
- [v1.0.6 -> v1.1.0](#v110)
- [v1.1.0 -> v1.2.0](#v120)
- [v1.2.0 -> v1.2.1](#v121)
- [v1.2.1 -> v1.3.0](#v130)
- [v1.3.0 -> v1.3.1](#v131)
- [v1.3.1 -> v1.3.5](#v135)
- [v1.3.5 -> v1.3.6](#v136)
- [v1.3.6 -> v1.3.7](#v137)
- [v1.3.7 -> v1.4.0](#v140)


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

## v1.2.1

### Bug Fixes

- **Meraki SDK v1.7.0+ errors (#3)**
    - ISSUE: The Meraki SDK introduced a 'batch' directory which contains special classes and methods within those classes. This nested structure breaks how Meraki-CLI parses the SDK to build its parser and documentation due to it expecting a flat predictable structure (classes in the API object, methods in those classes).
    - FIXES: v1.2.1 locks the Meraki SDK dependency to v1.6.2. Currently in the process of converting all of Meraki-CLI's parsing to recursive to better handle changing structures like this. A proper recursive version will be released soon in v1.3.0. v1.2.1 is a simple quick patch for this issue.

## v1.3.0

### Bug Fixes

- **Recursive parsing of Meraki SDK (#3)**
    - ISSUE: See the bug referenced in [v1.2.1](#v121). This version (v1.3.0) implements a permanent fix for the issue described here.
    - FIXES: v1.3.0 converts the static, nested, for-loops previously used to iterate through Meraki' library (to build the parser and documentation) into a recursive loop which iterates down to an unspecified depth in order to build the parser and documentation system. This functionality provides much better adaptation to future changes by Meraki to their library structure.

- **Daily testing**
    - ISSUE: Meraki-CLI v1.2.1 was released on 2021-03-29 in response to a change in Meraki's library (which broke Meraki-CLI) which occurred on 2021-03-16. From 2021-03-16 to 2021-03-29 any installation of Meraki-CLI was inherently broken due to this incompatibility. No system was present to report issues with the Meraki-CLI library. The problem was reported via an opened Github issue as well as comments on a social media platform. It is unacceptable to allow this library to remain inherently broken for that long with no attention.
    - FIXES: The incompatibility problem is easily caught by the CI system used for Meraki-CLI testing. However, because the testing only executes when commits are made to the repo, it was not caught during the 13 days it was broken. To remedy this, daily testing has been scheduled in the CI system which will run the full Meraki-CLI test suite and send out notifications if any tests fail.

## v1.3.1

### Bug Fixes

- **v1.2.1 version lock not removed**
    - ISSUE: v1.3.0 release did not remove the version lock to an older (compatible) version of the Meraki SDK which was imposed on v1.2.1.
    - FIXES: The version lock has been lifted and newer versions of the Meraki SDK can be installed now.

- **New recursive parser builder function not explicitly tested**
    - ISSUE: v1.3.0 moved the recursive analysis of the Meraki SDK and the building of the parser into its own function. An explicit test for this new function was not also created in the process. A new test has now been created to test this function.

## v1.3.5

### Bug Fixes

- **Positional arguments were not being parsed as JSON**
    - ISSUE: Positional arguments which had annotated types of list or dict would be be parsed as JSON. See #9. For example `createNetworkSwitchStack` used with `--serials '["1111-1111-1111", "2222-2222-2222"]'` would not interpret the JSON data into a Python list before passing it to the method. This could be worked around by using `--serials 1111-1111-1111 --serials 2222-2222-2222`, but having JSON decoding would be nice.
    - FIXES: Added tests to detect this issue  and heavily modified `_get_method_params()` to parse as JSON only when the proper annotations existed in the method params.

## v1.3.6

### Misc
- **Python 3.10 Support**
    - Full testing against Python 3.10 versions has been added.

- **Python Version in `-v` switch**
    - The `meraki -v` command will now include the current Python interpreter version.

- **Local version testing with Tox**
    - Config files and instructions have been added to streamline testing against multiple Python versions locally.

### Bug Fixes

- **Exception logging**
    - ISSUE: Some logging testing was malfunctioning but was not throwing errors until tested in 3.10.
    - FIXES: The logging has been fixed to meet the test criteria.

## v1.3.7

### Bug Fixes

- **Object filtering using inconsistent object keys (#10)**
    - ISSUE: Some Meraki API endpoints return inconsistent keys in their data. An example of this is the `switch getDeviceSwitchPortsStatuses` command/function which will return lldp keys and values for a port only when data exists to populate the value. Filtering on these inconsistent keys was impossible. The `_object_filter()` function would raise an exception and stop execution if this was encountered. Much more information can be found in Issue #10 where this problem is described in detail.
    - FIXES: The `_object_filter()` function has been extended to better handle inconsistent keys. It is also now being tested to filter complex fields.

## v1.4.0

### New Features

- **Tab Autocompletion on Linux and MacOS**
    - Meraki-CLI now supports tab autocompletion of all commands, switches, and arguments on Linux, MacOS, and limited support on Windows 10. Enablement of autocompletion requires a few steps after upgrade/installation of the Meraki-CLI package. Steps can be found in the [Tab Autocompletion](https://github.com/PackeTsar/meraki-cli/#tab-autocompletion) section of the README.
