'''Multiply funtion'''
import sys
import logging
from app.commands import Command


class MultiplyCommand(Command):
    '''ultiplyCommand'''
    def execute(self):
        logging.info('I will multiply a number')

    def undo(self):
        '''Undo fuction'''
        logging.info('Undo the Multiply')
