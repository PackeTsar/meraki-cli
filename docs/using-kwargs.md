---
title: Using Kwargs
---

# Using `--kwargs`

Some Meraki-CLI commands require arguments to be provided which are not explicitly defined in the underlying function, but are documented in the command help page. An example of this is the `updateDeviceSwitchPort` command. You can see an example of this command's help page in the [Making Some Changes](making-some-changes/) section.

In the command help page you will see many argument options under the "All Arguments" section, but only two of them are listed in the "Required Arguments" section: `serial` and `portId`. Some of the other arguments in the documentation are things like `name`, `tags`, `enabled`, etc.

---

When arguments are not listed in the "Required Arguments" or "Misc Arguments" sections of the command help page, they are considered to be Optional Arguments.

Optional Arguments can be provided in one of two ways:

1. Using regular CLI arguments like `--name "Test Name"` and `--vlan 100`
2. Nested as JSON data inside the `--kwargs` argument like `--kwargs '{"name": "Test Name", "vlan": "100"}'`
   - On Windows CLI, you have to use double-double quotes inside the data like `--kwargs "{""name"": ""Test Name"", ""vlan"": ""100""}"`

When Optional Arguments are provided at the command-line (in either of the above two ways), they are parsed into native data types and are included as `**kwargs` to the underlying target method when it is called.

!!! note
    Remember that Meraki-CLI is a wrapper on top of the [Meraki Dashboard API Python SDK](https://github.com/meraki/dashboard-api-python){:target="_blank"}, which is a Python library and includes programmatic functions. Each Meraki-CLI command (ie: `updateDeviceSwitchPort`) corresponds to one of those functions.

---

Some arguments cannot be simple data types, for example the `--tags` argument from the `updateDeviceSwitchPort` command.

The `--tags` argument must be an array, not a simple string or integer.

Again there are two ways you can provide this value:

1. Use the `--tags` option and provide a JSON-parsable array like: `--tags '["first_tag", "second_tag"]'`
2. Use the `--kwargs` option to provide the nested JSON data like `--kwargs '{"tags": ["first_tag", "second_tag"]}'`

Both of these options will result in the same data being sent to the underlying target method.

---

## Dealing With `--kwargs` in Windows

The `--kwargs` data passed into Meraki-CLI is a JSON string and the JSON standard requires double-quotes in the data for quoting; it does not allow single-quotes.

This becomes challenging on a standard Windows command prompt because Windows usually wants double-quotes used to encapsulate a string on the CLI.

---

So how do you use double quotes in the data and to encapsulate it?

To do this, use regular double-quotes in front of and behind the string to encapsulate it, and you use double-double-quotes in the actual data.

That means replacing all uses of double-quote characters in the data with two double-quotes.

Your argument ends up looking like

```
--kwargs "{""name"": ""Data Port"", ""vlan"": ""100""}"
```

It is probably easiest to use find/replace in a text editor to do this for you.

---

## Add Some Structure

You can also structure the JSON data and your command a bit if you want to make your command more readable.

In Windows, you can do this by ending each line with a carat (`^`) which will allow the command to continue on the next line.

Your command in this example will look like:

```
meraki switch updateDeviceSwitchPort --serial 1234-ABCD-5678 --portId 24 --kwargs ^
"{ ^
    ""name"": ""Data Port"", ^
    ""vlan"": ""100"", ^
}"
```
