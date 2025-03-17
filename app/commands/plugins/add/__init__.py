'''add funtion'''
import sys
import logging
from app.commands import Command


class AddCommand(Command):
    '''AddCommand'''
    def execute(self):
        logging.info('I will add the number')

    def undo(self):
        '''Undo fuction'''
        logging.info('Undo the add')
