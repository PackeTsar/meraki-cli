#!/usr/bin/env python3

"""
Script to automatically build the command guide by parsing the SDK.
"""


# Built-in libraries
import re

# Installed libraries
import meraki
from jinja2 import Template

# Local libraries
import meraki_cli as cli


def _get_structure() -> {}:
    """
    Build a dict structure of the parsable CLI arguments. This will be passed
        into the J2 template and iterated to build the command guide.
    FIXME: This code also exists in cli.__main__, need to find a way to DRY it
        up.
    """
    # Instantiate a fake instance of the API so we can parse it and build the
    #     argparse structure from it
    api = meraki.DashboardAPI('fake_key', suppress_logging=True)
    result = {}
    # Iterate class strings and classes in the fake API instance
    for clsstr, cls in api.__dict__.items():
        if clsstr[0] == "_":  # If this is a private attribute
            continue  # Don't add it to the argument parser
        clsmtds = {}
        result[clsstr] = clsmtds
        # For method string in the class
        for mtdstr in dir(cls):
            if mtdstr[0] == "_":  # Skip if private
                continue
            # Instantiate an Args object to parse the parameters required by
            #     the method and make them easy to access.
            clsmtds[mtdstr] = cli.Args(getattr(cls, mtdstr))
    return result


def _uri_name(name: str) -> '':
    """
    Generate a URI name for the method which matches what Markdown will want
        to use for deep linking. IE: 'updateVlan' becomes 'update-vlan'
    """
    # Create the title name of the method by splitting on caps. _cmd_title
    #     will turn 'claimIntoOrganization' into 'Claim Into Organization'.
    titleName = cli.__main__._cmd_title(name)
    # Replace whitespace with dashes and lowercase everything
    return titleName.replace(' ', '-').lower()


def _cmd_section(arg_obj: cli.Args) -> '':
    """
    Generate a portion of the help section for the page from the method
        docstring. Unindent the lines a bit so they can be used for markdown.
    """
    docstr = arg_obj.method.__doc__  # Start with the docstring
    result = ''  # And an empty result
    for line in docstr.splitlines():  # Iterate the lines
        result += f'\n{line.lstrip()}'  # And strip the leading whitespace
    # Grab the description line which is wrapped in double asterisks like
    #     '**this**' and has a newline immediately following. And add an
    #     additional newline after it to help with Markdown formatting.
    result = re.sub(r'(\*\*.*\*\*\n)', r'\1\n', result)
    # Grab each of the bullet point parameter names and wrap the name in
    #     backticks for markdown formatting.
    result = re.sub(r'- ([a-zA-Z]+)', r'- `\1`', result)
    return result


def _cmd_args(arg_obj: cli.Args) -> '':
    """
    Build an example of how to use the arguments with a function. Take the
        positional parameters like ['networkId', 'name'] and generate a string
        like "`--networkId 'STRING' --name 'STRING'" which can be used to
        provide an example in the command guide.
    """
    result = ''
    for arg in arg_obj.positionals:  # Iterate the positional parameters
        if arg.annotation is bool:  # If it is annotated as a boolean
            metavar = ''  # It is a switch. No value needed
        elif arg.annotation is str:  # If it is a regular string
            # Wrap the value example in quotes as is a good practice and look
            #     up the metavar we use to provide a value example
            metavar = " '"+cli.ANNOTATION_MAP[arg.annotation]['metavar']+"'"
        else:
            # Otherwise just add the regular metavar
            metavar = ' '+cli.ANNOTATION_MAP[arg.annotation]['metavar']
        # Build the argument example and add it to the result
        result += f' --{arg.name}{metavar}'
    return result


def main() -> None:
    """
    Primary function called from native script.
    """
    struct = _get_structure()  # Grab the structure dict of the arguments
    # Read in the Jinja2 template file
    f = open('.command_guide_template.md', 'r')
    template = Template(f.read())  # Load the template data
    f.close()
    # Render the Jinja2 template using needed variables
    guidestr = template.render(
        version=meraki.__version__,
        struct=struct,
        _cmd_title=cli.__main__._cmd_title,
        _cmd_section=_cmd_section,
        _cmd_args=_cmd_args,
        _uri_name=_uri_name,
        )
    # Write the template rendering to the final command guide markdown file
    guide = open('COMMAND_GUIDE.md', 'w')
    guide.write(guidestr)
    guide.close()


if __name__ == "__main__":
    main()
