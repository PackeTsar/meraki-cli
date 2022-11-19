---
title: Try It Out
---

You can kick the tires on Meraki-CLI using **Cisco's DevNet Code Space**

[![meraki-cli-exchange-devenv](https://raw.githubusercontent.com/CiscoDevNet/code-exchange-repo-template/master/manual-sample-repo/img/meraki-cli-exchange-devenv.png)](https://developer.cisco.com/codeexchange/github/repo/PackeTsar/meraki-cli){:target="_blank"}


## Step 1: Open a Code Space

- Go to the [Meraki-CLI DevNet page](https://developer.cisco.com/codeexchange/github/repo/PackeTsar/meraki-cli){:target="_blank"}
- Click on the green "**Try it out!**" button
    - You may need to log in to DevNet using your Cisco ID
- Once the Code Space is opened, you will see a CLI terminal at the bottom of the page which looks like the below

![code-space-terminal](code_space_terminal.jpg)


## Step 2: Install Meraki-CLI

- In this terminal, run the command to install Meraki-CLI: `pip3 install meraki-cli`
- Once the installation is finished, enable tab auto-completion with: `eval "$(register-python-argcomplete meraki)"`
- Now you should be able to type in `meraki`, hit the TAB key twice, and see a list of commands
- If you hit ENTER with just `meraki` typed in the prompt, it will output the help page


## Step 3: Get your Meraki API Key

To allow Meraki-CLI to access your Meraki Dashboard, you will need to enter your Meraki API key into this prompt as an environment variable using the `export MERAKI_DASHBOARD_API_KEY=my_api_key` syntax

Once you have entered your API key, you will be able to start running Meraki-CLI commands against your Meraki Dashboard!
  
Click the "Next" button below to continue on to the API key instructions page

---

[Next: Getting Your API Key :octicons-arrow-right-24:](../getting-your-api-key/){ .md-button .md-button--primary }
