---
title: Update/Upgrade
---

??? info "Updating from Pre-1.5.0?"

    Meraki-CLI version 1.5.0 introduced the native upgrade capability. Use these commands if you are running a version older than v1.5.0

    === ":material-lightbulb: PIP (Recommended)"

        ```
        pip3 install --upgrade --no-cache-dir meraki-cli
        ```

    === ":material-language-python: via Python"

        ```
        python3 -m pip install --upgrade --no-cache-dir meraki-cli
        ```

## Update/Upgrade

Starting with v1.5.0, Meraki-CLI and its dependencies can be updated to the latest version using the Meraki-CLI `meraki` CLI tool itself.

=== "Meraki-CLI and SDK (Recommended)"

    ```
    meraki upgrade --upgrade-all
    ```

=== "Meraki-CLI Only"

    ```
    meraki upgrade --upgrade-meraki-cli
    ```

=== "Meraki SDK Only"

    ```
    meraki upgrade --upgrade-meraki-sdk
    ```

=== "Meraki-CLI, SDK, and all dependencies"

    ```
    meraki upgrade --upgrade-all-eager
    ```

---
