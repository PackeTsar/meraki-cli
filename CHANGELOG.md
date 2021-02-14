###  [< (Back) to Meraki-CLI Home](https://github.com/PackeTsar/meraki-cli/)


# Meraki-CLI Version Change Log

Documented below is a history of Meraki-CLI versions and a log of changes to each version


# Table of Contents
- [v1.0.5 -> v1.0.6](#v1-0-6)


# Versions

## v1.0.6

### Bug Fixes

- **Cryptic error with malformatted translation**
    - ISSUE: When a poorly formatted translation is entered, the error is not easy to understand. It is a generic Python exception
    - FIXES: 20cfc8c07c7cbd09e1f9c684eb14a33ee2bf4cc7
- **Error Kills Looped Execution**
    - ISSUE: Looped execution (like when pipelining) can be broken by a single error in one of the execution events. This can be seen by issuing `meraki organizations getOrganizations | meraki -t "organizationId=id" organizations getOrganizationNetworks` when at least one of the organizations is not API-enabled. May want to add error catching or control when performing looped execution.
    - Fixes: 800727df6a7cc24d18e0c6ac751714ec2f4498bf
