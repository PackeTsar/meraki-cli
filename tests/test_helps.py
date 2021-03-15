import unittest
import os
from meraki_cli.__main__ import _cmd_title, _cmd_help


class TestHelps(unittest.TestCase):

    def setUp(self):
        # Use the importlib to help import the _get_structure builder from the
        #     command guide builder file
        from importlib.machinery import SourceFileLoader
        # Get the directory of this file
        filedir = os.path.abspath(os.path.join(__file__, os.pardir))
        # Get the parent dir of this dir
        pardir = os.path.dirname(filedir)
        # Build the path to the .command_guide_build.py file
        builderfile = os.path.join(pardir, '.command_guide_build.py')
        # Create a module out of the command guide builder file
        self.builder = SourceFileLoader('builder', builderfile).load_module()
        # Grab the class and method structure
        struct = self.builder._get_structure()
        self.arg_object_list = []  # Make a list to contain all the arg objects
        # Iterate the structure
        for className, mtdDict in struct.items():
            for mtdName, argObject in mtdDict.items():
                # And add the argument object to the list
                self.arg_object_list.append(argObject)

    def testTitle(self):
        assert _cmd_title('oneTwoThree') == 'One Two Three'
        assert _cmd_title('OneTwoThree') == 'One Two Three'
        assert _cmd_title('onetwoThree') == 'Onetwo Three'

    def testAllCmdGuideCmdSections(self):
        """
        Test generating command guide help sections for each method
        """
        for argObject in self.arg_object_list:
            # And test building the command section for each arg object
            self.builder._cmd_section(argObject)

    def testAllCmdGuideCmdArgExamples(self):
        """
        Test generating example arguments for each method
        """
        for argObject in self.arg_object_list:
            # Test building the example arg list for this object
            self.builder._cmd_args(argObject)

    def testAllCLIHelpPages(self):
        """
        Test the help page modifications for every available function
        """
        for argObject in self.arg_object_list:
            # And test building a CLI help page for every method
            _cmd_help(argObject)
