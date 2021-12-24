# Tab Autocompletion for Meraki-CLI tool
autoload bashcompinit
bashcompinit
autoload compinit
compinit -u
eval "$(register-python-argcomplete meraki)"
# End of Meraki-CLI commands
