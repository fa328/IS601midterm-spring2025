'''subtrat funtion'''
import sys
import logging
from app.commands import Command


class SubtractCommand(Command):
    '''SubtractCommand'''
    def execute(self):
        logging.info('I will subtract a number')

    def undo(self):
        '''Undo fuction'''
        logging.info('Undo the subtraction')
