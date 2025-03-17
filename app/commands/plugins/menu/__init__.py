'''add funtion'''
import sys
import logging
from app.commands import Command


class MenuCommand(Command):
    '''MenuCommand'''

    def execute(self):
        logging.info('I will add a menu')

    def show_menu(self):
        '''to show the menu option'''
        logging.info('list of available options.')

    def add_option(self, option):
        '''to add menu option'''
        logging.info('Adding menu option: %s', option)
