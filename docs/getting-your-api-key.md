---
title: Getting Your API Key
---

In order to operate the CLI you need to input your Meraki API key. The API key will be a string of random hex digits.

!!! warning
    In order to use Meraki-CLI (and the Meraki API in general), your organization needs to have **Dashboard API access** enabled. Do this in the Meraki Dashboard by navigating to **Organization** > **Configure** > **Settings**, then making sure the **API Access** checkbox is checked in the **Dashboard API access** section.

You can obtain your Meraki API key by:

- Logging into the [Meraki Dashboard](https://dashboard.meraki.com){:target="_blank"}
- Clicking your user name in the top right corner
- Clicking on **My profile**
- View the 'API Access' section near the bottom of the page
- Click on the '**Generate new API key**' button and copy down your new API key before saving. It will be a long hexadecimal string.

---

Plug your API key into Meraki-CLI using one of three methods:

??? info "Example API Key"
    The API key seen in the examples is a public one Meraki provides for testing against their sandbox networks. Feel free to use it for testing things out, but sometimes it gets overused and is throttled by Meraki. Meraki also may also change it in the future. All the output examples shown below use that key.

=== ":material-clock-fast: Environment Variable (Fastest)"

    Open your command-line terminal and run the below command to temporarily store your API key as an environment variable.

    === ":material-microsoft-windows: Windows"

        ```
        set MERAKI_DASHBOARD_API_KEY=6bec40cf957de430a6f1f2baa056b99a4fac9ea0
        ```

    === ":material-apple: MacOS"

        ```
        export MERAKI_DASHBOARD_API_KEY=6bec40cf957de430a6f1f2baa056b99a4fac9ea0
        ```

    === ":fontawesome-brands-linux: Linux"

        ```
        export MERAKI_DASHBOARD_API_KEY=6bec40cf957de430a6f1f2baa056b99a4fac9ea0
        ```


=== ":material-file-cog: Config File (Recommended)"

    This method requires creating a config file for Meraki-CLI in a certin directory based on your specific operating system.

    See the [Using a Config File](../using-a-config-file/) section for more info on how to do this.


=== ":fontawesome-solid-terminal: CLI Argument"

    Use the `-k` or `--apiKey` argument at the top level of the command like:

    ```
    meraki -k 6bec40cf957de430a6f1f2baa056b99a4fac9ea0 ...
    ```

---

After you have set Meraki-CLI up to use your API key, you'll want to try running [A Few Starting Commands](../a-few-starting-commands/).

[Next: A Few Starting Commands :octicons-arrow-right-24:](../a-few-starting-commands/){ .md-button .md-button--primary }
