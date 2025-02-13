import logging

from .startup import *

class Program():
    """ Abstract class that processes command line arguments as files. """

    def __init__(self):
        """ Initialize the application.

            :settings: `dict` containing configuration variables, environment
                       variables, and command line arguments.
        """
        log.info("Initializing Program class...")
        