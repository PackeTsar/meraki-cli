import unittest
import os
import requests_mock
from meraki_cli import __main__, _user_agent
from urllib.parse import unquote


class TestUserAgent(unittest.TestCase):
    """
    Test that the Meraki Dashboard SDK is properly inserting our User-Agent
        string into its HTTP requests.

    Test must be run twice because the meraki.DashboardAPI() object is
        instantiated in two different ways in __main__.main():
        1. While providing the apiKey explicitly like DashboardAPI(apiKey=...)
        2. While allowing the Meraki SDK to pull the key from env variables
    """

    def text_callback(self, request, context):
        """
        Method for analyzing request and providing response. Used to inspect
            the request headers, specifically the User-Agent header to make
            sure it contains our Meraki-CLI caller string.
        """
        context.status_code = 200  # Set status code for response
        # Grab and decode the User-Agent header from the Meraki HTTP call to
        #     the Dashboard API
        user_agent = unquote(request._request.headers['User-Agent'])
        # If our standard Meraki-CLI User-Agent string is not in there
        if _user_agent not in user_agent:
            # Fail the test and provide info
            raise Exception(f'User-Agent Incorrect: {user_agent}')
        return '{}'  # Return a JSON parsable string to make SDK happy

    def testUserAgentWithExplicitKey(self):
        # Intercept calls from the Python requests library
        with requests_mock.Mocker() as mock:
            # Intercept all requests calls and process them through the
            #     text_callback() method.
            mock.get(requests_mock.ANY, text=self.text_callback)
            # Set to true to prevent processing as an instance feeding from
            #     STDIN
            __main__.NO_STDIN = True
            # Execute the main program with some arguments. Provide the API
            #     key explicitly in the arguments
            __main__.main(
                argstring='-k 12345 -dddd organizations getOrganizations')

    @unittest.mock.patch.dict(  # Mock an environment variable for the API key
        os.environ, {'MERAKI_DASHBOARD_API_KEY': '12345'})
    def testUserAgentWithEnvironmentKey(self):
        # Intercept calls from the Python requests library
        with requests_mock.Mocker() as mock:
            # Intercept all requests calls and process them through the
            #     text_callback() method.
            mock.get(requests_mock.ANY, text=self.text_callback)
            # Set to true to prevent processing as an instance feeding from
            #     STDIN
            __main__.NO_STDIN = True
            # Execute the main program with some arguments. Allow the API key
            #     to be pulled from the mocked environment variable
            __main__.main(
                argstring='-dddd organizations getOrganizations')
