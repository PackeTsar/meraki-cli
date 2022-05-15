---
title: Using a Config File
---

If you find yourself regularly entering the same arguments into the Meraki-CLI tool like your API key, debug level, logfile, etc, it might make sense to save those settings to a static config file in a permanent location.

The Meraki-CLI tool supports the use of a config file to provide any of its arguments. The config file should contain proper JSON syntax and should be a simple object (Python dictionary) in format. An example is shown below.

!!! tip "Get Config File Settings From Command"
    If you want to use the arguments of a currently working command for your config file, set a maximum debug level of `-ddd` and copy/paste the JSON output under the "Argument Settings" log statement.

## Config File Location

The config file can be obtained by the program by either explicitly defining its location using the `-c` option like `-c ~/meraki-cli.conf`, or by placing the file in a location searched by Meraki-CLI upon program start. The search locations are provided below.

=== ":material-microsoft-windows: Windows 10/11 WSL or :fontawesome-brands-linux: Linux"

    The below file paths are searched in this order for a Meraki-CLI config file on Linux or WSL.

    1. `./meraki-cli.conf` (current working directory)
    2. `~/.meraki-cli/meraki-cli.conf` (hidden directory in user's home directory)
    3. `/etc/meraki-cli/meraki-cli.conf`

=== ":material-apple: MacOS"

    The below file paths are searched in this order for a Meraki-CLI config file on MacOS.

    1. `./meraki-cli.conf` (current working directory)
    2. `~/.meraki-cli/meraki-cli.conf` (hidden directory in user's home directory)
    3. `~/Library/Application Support/meraki-cli/meraki-cli.conf`

=== ":material-microsoft-windows-classic: Windows Native"

    The below file paths are searched in this order for a Meraki-CLI config file on native Windows.

    1. `%APPDATA%\meraki-cli\meraki-cli.conf`
        - ??? info "The `%APPDATA%` Directory"
            The `%APPDATA%` directory is usually equal to `C:\Users\<username>\AppData\Roaming` by default.
            Assuming the default, the config file location would be: `C:\Users\<username>\AppData\Roaming\meraki-cli\meraki-cli.conf`

    2. `%LOCALAPPDATA%\meraki-cli\meraki-cli.conf`
        - ??? info "The `%LOCALAPPDATA%` Directory"
            The `%LOCALAPPDATA%` is usually equal to `C:\Users\<username>\AppData\Local` by default.
            Assuming the default, the config file location would be: `C:\Users\<username>\AppData\Local\meraki-cli\meraki-cli.conf`

!!! note "All Paths are Searched"
    Any of the above locations except `/etc/meraki-cli/meraki-cli.conf` will work on any platform.

    - The `APPDATA` and `LOCALAPPDATA` environment variables exist on Windows by default, but can be added to any machine
    - The two `~` (home) locations will resolve on both Windows or MacOS/Linux to a subdirectory inside the user's home directory.


---

## Example `meraki-cli.conf` Config File

```json
{
    "apiKey": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
    "debug": 1,
    "logfile": "meraki.log"
}
```

---

## Creating Your Config File

=== ":material-microsoft-windows: Windows 10/11 WSL | :fontawesome-brands-linux: Linux | :material-apple: MacOS"

    1. Create the hidden `.meraki-cli` directory in your home directory
        ```
        mkdir ~/.meraki-cli
        ```
    2. Create a new file called `meraki-cli.conf` in the new directory
        ```
        nano ~/.meraki-cli/meraki-cli.conf
        ```
    3. Copy and paste the contents of the example file from above into the editor
    4. Edit the API key and change/remove other settings if desired
    5. Use CTRL-X to prompt for exit
    6. Press the "Y" key to save the file
    7. Press ENTER to confirm the file name

=== ":material-microsoft-windows-classic: Windows Native"

    1. Open a text editor
    2. Create a new text file at path: `C:\Users\<username>\AppData\Roaming\meraki-cli\meraki-cli.conf`
    3. Copy and paste the contents of the example file from above into the editor
    4. Edit the API key and change/remove other settings if desired
    5. Save the file
