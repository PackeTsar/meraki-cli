#!/usr/bin/python


'''
Basic utility functions used by meraki-cli features
'''


import json
import logging


log = logging.getLogger('meraki-cli')


def attrib_expression(strlist):
    '''
    Interpret a list of command-line expressions into an attribute dict
    '''
    result = {}  # Result should be a flat dict
    for expr in strlist:
        try:  # See if the expression is legit JSON
            data = json.loads(expr)  # Try to load it up, will except if bad
            log.info(f'Expression ({expr}) read as JSON: {data}')
            if type(data) != dict:  # Make sure it is a flat dict
                log.warning(f'Error with JSON data, must be dict: {data}')
            else:
                result.update(data)
            continue
        # No problem if not JSON, we will interpret
        except json.decoder.JSONDecodeError:
            log.debug(f'Expression ({expr}) not valid JSON data')
        if ':' not in expr:  # Not a valid key/val expression if no ':'
            log.warning(f'Colon (:) not found in expression ({expr})')
            continue
        words = expr.split(':')  # Split into a list of terms
        val = ''.join(words[1:])  # Create the value side of the attrib
        # Detect boolean values and set appropriately
        if val.lower() == 'true':
            val = True
        elif val.lower() == 'false':
            val = False
        # Create attribute and plop into result
        newattrib = {words[0]: val}
        result.update(newattrib)
    return result
