---
title: Complex Argument Values
---

Sometimes it is necessary to provide more complex values in certain arguments. An example from the `meraki switch updateDeviceSwitchPort` command is the `--tags` argument.

```
~$
~$ meraki switch updateDeviceSwitchPort -h
...
All Arguments:
  --serial (string): (required)
  --portId (string): (required)
  --name (string): The name of the switch port
  --tags (array): The list of tags of the switch port
...
~$
~$
```

The `--tags` argument requires a list (array) of items. You can provide this list of items at the CLI using JSON formatting.

This will look like:

- :fontawesome-brands-linux: Linux/WSL/MacOS shell: `--tags '["tag1", "tag2"]'`
- :material-microsoft-windows: Windows native shell: `--tags "[""tag1"", ""tag2""]"`

This formatting provides a JSON-parsable structure to the CLI tool which is turned into native data and sent over the API to the dashboard.

!!! info "Advanced `--kwargs` Arguments"
    If you want to dive deeper into how to provide JSON data at the CLI, check out the [Using --kwargs](/using-kwargs) and [Dealing with --kwargs in Windows](/using-kwargs/#dealing-with-kwargs-in-windows) sections.
