---
title: Tab Auto-Completion
---

Meraki-CLI v1.4.0 introduced tab autocompletion support on MacOS (zsh), Linux (bash), and Windows 10/11 Subsystem for Linux (WSL) using the Python [argcomplete](https://github.com/kislyuk/argcomplete){:target="_blank"} framework. Once you have installed Meraki-CLI, there are a few additional steps you need to take to enable autocompletion. See below for these steps.

Once tab autocompletion is functional, you will be able to hit the TAB key at any point in the command to see your options and/or complete a partial command. You are also able to set the `-h` switch at any point in the command and hit ENTER to see the help page for that specific command.

=== ":material-microsoft-windows: Windows 10/11 WSL"

    ??? warning "Tab Auto-Completion Only Supported on WSL"

        A native installation of Meraki-CLI on Windows (where you use the Windows Command Prompt for the `meraki` commands) does not support tab autocompletion.

        In order to use the tab-autocompletion feature in Windows, you need to [Install on Windows 10 WSL](step-by-step_installation/). Once Meraki-CLI is installed, you can enable tab-autocompletion in WSL using the below steps.

    - Run `sudo activate-global-python-argcomplete` in WSL to activate the tab autocompletion feature
    > NOTE: We are running this as `sudo` on purpose. The autocomplete feature must be installed and activated at the global level
        - You should just see the response "Installing bash completion script /etc/bash_completion.d/python-argcomplete"
    - Exit the WSL window with `exit`
    - Reopen the WSL command window by finding the "Ubuntu" app in your start menu
    - Run the `meraki` command and make sure you see the help output
    - Type `meraki` at the prompt and then hit the TAB key a few times
    - You now should see all the arguments/switches/commands available to you

=== ":material-apple: MacOS"

    If you are using the terminal on a modern version of MacOS, you are probably using zsh ("z shell") instead of bash, which is the standard for Linux distros. Use one of the two below options to enable autocompletion for your terminal:

    === ":material-check-bold: Option 1 (Easy)"

        - Run the below command to populate your zsh profile with the proper commands
            ```
            curl -fs https://raw.githubusercontent.com/PackeTsar/meraki-cli/master/.zprofile >> ~/.zprofile
            ```
        - Exit your terminal application and re-open it
        - Type `meraki` at the prompt and then hit the TAB key
        - You now should see all the arguments/switches/commands available to you

    === ":octicons-file-code-24: Option 2 (Manual)"

        - Open your zsh profile file with `nano ~/.zprofile`
        - Add the below text to the bottom of the file

        ```
        # Tab Autocompletion for Meraki-CLI tool
        autoload bashcompinit
        bashcompinit
        autoload compinit
        compinit -u
        eval "$(register-python-argcomplete meraki)"
        # End of Meraki-CLI commands
        ```

        - Once the text is added, press **CTRL-X**, hit the '**y**' key, and hit **ENTER** to save the changes to the file
        - Exit your terminal application and re-open it
        - Type `meraki` at the prompt and then hit the TAB key
        - You now should see all the arguments/switches/commands available to you


=== ":fontawesome-brands-linux: Linux"

    - At your CLI terminal, run the command `activate-global-python-argcomplete`
      - If you are using a Redhad distro like CentOS, also run the command `echo 'eval "$(register-python-argcomplete meraki)"' >> ~/.bash_profile`
    - Exit the terminal session and restart it (log out and back in if on SSH)
    - Type `meraki` at the prompt and then hit the TAB key
    - You now should see all the arguments/switches/commands available to you

---

Once Tab Auto-Completion has been enabled, follow the instructions in [Getting Your API Key](getting-your-api-key/) section to obtain and plug-in your Meraki Dashboard API key.
