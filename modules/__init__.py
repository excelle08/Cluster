from abc import ABCMeta, abstractmethod

class Command(object):
    """docstring for Command"""

    __metaclass__ = ABCMeta

    def __init__(self):
        super(Command, self).__init__()
    
    @abstractmethod
    def name(self):
        return ''
        
    @abstractmethod
    def intro(self):
        return ''

    @abstractmethod
    def help(self):
        return ''

    @abstractmethod
    def execute(self, argv):
        return 0

