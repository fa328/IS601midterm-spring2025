'''divide funtion'''
import sys
import logging
from app.commands import Command


class DivideCommand(Command):
    '''DividetCommand'''
    def execute(self):
        logging.info('I will divide a number')

    def undo(self):
        '''Undo fuction'''
        logging.info('Undo the divide')
