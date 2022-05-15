---
title: Step-by-Step Installation
---

## Step-by-Step Installation

<p align="center">
  <iframe width="800" height="315 allowfullscreen"
    src="https://www.youtube.com/embed/uDfMvu_1rag">
  </iframe>
</p>

=== ":material-microsoft-windows: Windows 10/11 WSL (Recommended for Windows)"

    The **recommended** (but not only) way to run Meraki-CLI on Windows is to run it on [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about){:target="_blank"} (WSL). This is because Meraki-CLI's tab-autocompletion feature is only supported on MacOS and Linux platforms. Running it inside Windows 10 WSL gives you this full tab-autocompletion functionality.

    > **NOTE**: Running WSL version 2 (which is now the default) requires virtualization features to be enabled in your PC's BIOS settings. The settings may be called VT-x, AMD-V, or SVM.

    WSL is very quick and easy to install on your Windows 10/11 OS and should take about 10 minutes. Follow the below steps to install WSL, install Meraki-CLI, and set up tab-autocompletion.

    1. Click on the **Start** button and search for "features", click on the "**Turn Windows features on and off**" application
    2. Check the boxes for "**Virtual Machine Platform**" and "**Windows Subsystem for Linux**", click **OK** and reboot Windows once the     installation completes
    3. Once logged back in, click on the **Start** button and search for "store", open the "**Microsoft Store**" application
    4. Search for "ubuntu" inside the store and click on the "**Ubuntu 20.04**" app (or the latest version available), then click the     **Get** button to install it
    5. Once installation finishes, click the **Open** button to open WSL. It will ask you for a user name and password. Go through these     prompts to set up WSL
    6. After setting it up, you will have a command prompt with something like `user@MYWIN10PC:~$`. Now we will perform a Linux Meraki-CLI installation
    7. Run `sudo apt update` to pull the latest repository info
        - Provide your WSL password when prompted
    8. Run `sudo apt install python3-pip` to install the PIP Python package manager
    9. Run `sudo pip3 install meraki-cli` to install the Meraki-CLI tool
    10. Run `sudo activate-global-python-argcomplete` to activate the tab autocompletion feature
    >  NOTE: We are running this as `sudo` on purpose. The autocomplete feature must be installed and activated at the global level
        - You should just see the response "Installing bash completion script /etc/bash_completion.d/python-argcomplete"
    11. Exit the WSL window with `exit`
    12. Reopen the WSL command window by finding the "Ubuntu" app in your start menu
    13. Run the `meraki` command and make sure you see the help output
    14. Type `meraki` at the prompt and then hit the TAB key a few times
    15. You now should see all the arguments/switches/commands available to you

=== ":material-apple: MacOS"

    Meraki-CLI can be installed natively on MacOS and be used through the Terminal application. Follow the below steps to install Meraki-CLI on MacOS.

    - In order to use Meraki-CLI on MacOS, you need to have Python 3 installed. If you do not yet have Python 3 installed, visit this [Python 3 Installation Instructions Page](https://github.com/PackeTsar/Install-Python){:target="_blank"} and install for your operating system.
    - Once Python3 is installed, open your Terminal application by navigating in Finder to **Applications** > **Utilities** > **Terminal**
    - Run `pip3 install meraki-cli` to install the Meraki-CLI tool
    - Run the command `curl -fs https://raw.githubusercontent.com/PackeTsar/meraki-cli/master/.zprofile >> ~/.zprofile` to add commands to your terminal profile which will enable tab-autocompletion on startup
    - Close the Terminal application and re-open it
    - Run the `meraki` command and make sure you see the help output
    - Type `meraki` at the prompt and then hit the TAB key a few times
    - You now should see all the arguments/switches/commands available to you

=== ":material-microsoft-windows-classic: Windows 10/11 Native"

    The recommended way to run Meraki-CLI on Windows is to use the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about){:target="_blank"} (WSL) because it supports tab-autocompletion. But you can also install Meraki-CLI natively on Windows. Follow the below steps to install natively on Windows.

    - In order to use Meraki-CLI on native Windows, you need to have Python 3 installed. If you do not yet have Python 3 installed, visit this [Python 3 Installation Instructions Page](https://github.com/PackeTsar/Install-Python){:target="_blank"} and install for your operating system.
    - Once Python3 is installed, click on the **Start** button and search for "command", click on the "**Command Prompt**" application
    - Run `pip3 install meraki-cli` to install the Meraki-CLI tool
    - Run the `meraki` command and make sure you see the help output

=== ":fontawesome-brands-linux: Linux"

    The instructions here describe installation of Meraki-CLI on an Ubuntu 20 OS. Other distros may require slightly different commands.

    - Run `sudo apt update` to pull the latest repository info
      - Provide your password when prompted
    - Run `sudo apt install python3-pip` to install the PIP Python package manager
    - Run `sudo pip3 install meraki-cli` to install the Meraki-CLI tool
    - Run `sudo activate-global-python-argcomplete` to activate the tab autocompletion feature
    > NOTE: We are running this as sudo on purpose. The autocomplete feature must be installed and activated at the global level
        - You should just see the response "Installing bash completion script /etc/bash_completion.d/python-argcomplete"
    - Log out and back into the OS to restart BASH and enable tab-autocompletion
    - Run the `meraki` command and make sure you see the help output
    - Type `meraki` at the prompt and then hit the TAB key a few times
    - You now should see all the arguments/switches/commands available to you

---

Once fully installed, follow the instructions in [Getting Your API Key](../getting-your-api-key/) section to obtain and plug-in your Meraki Dashboard API key.
