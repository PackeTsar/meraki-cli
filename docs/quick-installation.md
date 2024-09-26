---
title: Quick Installation
---

Meraki-CLI is a standard Python package [published in the Python Package Index (PyPI)](https://pypi.org/project/meraki-cli/){:target="_blank"}. The recommended way to install Meraki-CLI is to use `pip` or `pipx`.

If you already have Python 3 installed on your operating system, use the commands below to install Meraki-CLI. To see full step-by-step instructions for your specific operating system, see the [Step-by-Step Installation](../step-by-step_installation/) section.

!!! note ":material-microsoft-windows: Windows Support"
    If you're using :material-microsoft-windows: Windows, it is recommended (but not required) to run Meraki-CLI on Windows Subsystem for Linux (WSL) to be able to use the [Tab Auto-Completion](../tab_auto-completion/) feature. See the [Step-by-Step Installation](../step-by-step_installation/) section for more info.

!!! note ":fontawesome-brands-linux: Modern Linux Support"
    Modern distributions of Linux (like Ubuntu24) lock down the native system Python packages to prevent users from breaking OS features when updating or changing those packages. The recommended way to install new Python packages is to use a virtual environment (venv).

    To install Meraki-CLI into a venv use the `pipx` commands as shown in the recommended steps below.

=== ":octicons-container-16: PIPX (Recommended for Linux or WSL)"

    ```
    sudo apt install pipx
    pipx ensurepath
    pipx install meraki-cli
    ```

=== ":material-lightbulb: Standard PIP"

    ```
    pip3 install meraki-cli
    ```

=== ":material-language-python: via Python"

    ```
    python3 -m pip install meraki-cli
    ```

---

Once installed, follow the instructions in the [Tab Auto-Completion](../tab_auto-completion/) section to enable autocompletion.

[Next: Tab Auto-Completion :octicons-arrow-right-24:](../tab_auto-completion/){ .md-button .md-button--primary }
