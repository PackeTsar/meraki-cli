import unittest
import os
from meraki_cli.__version__ import version


class TestDocVersions(unittest.TestCase):
    """
    Check that the README.md and CHANGELOG.md documentation files have been
        updated with the new Meraki-CLI version information before publication.
    """

    def checkFile(self, filename, find_string):
        # Get the directory of this file
        filedir = os.path.abspath(os.path.join(__file__, os.pardir))
        # Get the parent dir of this dir
        pardir = os.path.dirname(filedir)
        # Get the path of the file to open
        readme_file_path = os.path.join(pardir, filename)
        readmeFile = open(readme_file_path, 'r')
        readme = readmeFile.read()
        if find_string not in readme:  # If the string is not in the file
            raise Exception(  # Raise exception with info
                f'{filename} version does not match program version, cannot'
                f' find "{find_string}"')

    def testDocVersionsREADME(self):
        """
        Check that the README.md documented version matches program version
        """
        findstr = f'version of Meraki-CLI documented here is: **{version}**'
        self.checkFile('README.md', findstr)

    def testDocVersionsCHANGELOG(self):
        """
        Check that the CHANGELOG.md documented version matches program version
        """
        self.checkFile('CHANGELOG.md', f' -> v{version}')  # Check TOC
        self.checkFile('CHANGELOG.md', f'## v{version}')  # Check body
