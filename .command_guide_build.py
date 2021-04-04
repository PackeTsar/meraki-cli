#!/usr/bin/env python3

"""
Script to automatically build the command guide by parsing the SDK.
"""


# Built-in libraries
import re
import types

# Installed libraries
import meraki
from jinja2 import Template

# Local libraries
from meraki_cli.__main__ import Args
from meraki_cli import __main__ as climain


def _get_structure(result=None, obj=None, path=[]) -> dict:
    """
    Recursive function to build a dict structure of the parsable CLI
        arguments. This will be passed into the J2 template and iterated to
        build the command guide.
    """
    if not obj:  # If _get_structure() was called without arguments passed
        # Instantiate an API instance we can parse
        obj = meraki.DashboardAPI('fake_key', suppress_logging=True)
        result = {}  # Start with an empty dict as our result value
    if isinstance(obj, types.MethodType):  # If obj is a callable method
        arg_obj = Args(obj)  # Instantiate an Args() instance with it
        # Add its CLI path info as a string (command-path used to run it)
        arg_obj.path = ' '.join(path)
        return arg_obj  # And return it to be added to the result
    else:  # If obj is NOT a callable method
        # Iterate each attribute inside of it (as a string)
        for subobjstr in dir(obj):
            if subobjstr[0] == "_":  # If this is a private attribute
                # Skip this loop and don't add it to the argument parser
                continue
            # If it was not a private attribute
            path.append(subobjstr)  # Add the string to the command-path list
            # Grab the attribute object for this loop
            subobj = getattr(obj, subobjstr)
            if len(path) > 1:  # If out command-path is more than one command
                # Set the subobjstr to the full command path. This is used in
                #     the documentation in the section headers. It turns
                #     something like 'CreateNetworkApplianceStaticRoute' into
                #     'ApplianceCreateNetworkApplianceStaticRoute'. This helps
                #     prevent duplicate headers under the 'batch' command-path
                subobjstr = ' '.join(path)
            # Set a new key in the result to the output of a recursed
            #     iteration of this function. The output will be an Arg()
            #     instance if subobj is a callable method. Or it will be
            #     another dict if subobj is a class instance.
            result[subobjstr] = _get_structure(result={},
                                               obj=subobj,
                                               path=path)
            # Pop the last entry off of the path since we are ending a loop
            path.pop()
        # Return the result dict which was populated during the for loop
        return result


def _uri_name(name: str) -> str:
    """
    Generate a URI name for the method which matches what Markdown will want
        to use for deep linking. IE: 'updateVlan' becomes 'update-vlan'
    """
    # Create the title name of the method by splitting on caps. _cmd_title
    #     will turn 'claimIntoOrganization' into 'Claim Into Organization'.
    titleName = climain._cmd_title(name)
    # Replace whitespace with dashes and lowercase everything
    return titleName.replace(' ', '-').lower()


def _cmd_section(arg_obj: Args) -> str:
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
    # Add a '##### Arguments' line below the Meraki link and above the
    #     argument options.
    result = re.sub(r'(\nhttps://.*\n)', r'\1\n##### Arguments', result)
    # Grab each of the bullet point parameter names and wrap the name in
    #     backticks for markdown formatting.
    result = re.sub(r'- ([a-zA-Z0-9_]+) ', r'- `--\1` ', result)
    return result


def _cmd_args(arg_obj: Args) -> str:
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
            metavar = " '"+climain.ANNOTATION_MAP[
                arg.annotation]['metavar']+"'"
        else:
            # Otherwise just add the regular metavar
            metavar = ' '+climain.ANNOTATION_MAP[arg.annotation]['metavar']
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
        _cmd_title=climain._cmd_title,
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
