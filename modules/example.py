from modules import Command

class ExampleCmd(Command):
    def __init__(self):
        super(ExampleCmd, self).__init__()

    def name(self):
        return 'example'

    def intro(self):
        return 'This is an example command'

    def help(self):
        return 'Help message is here'

    def execute(self, argv):
        print 'If there to be a miracle, it must be orange.'
        return 0