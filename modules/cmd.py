from modules import Command
from cluster import configs
import common


class Cmd(Command):
    """docstring for Cmd"""
    def __init__(self):
        super(Cmd, self).__init__()

    def name(self):
        return 'cmd'

    def intro(self):
        return 'Execute a command on slave machines through SSH'

    def help(self):
        return 'Usage: cmd <Command>'

    def execute(self, argv):
        if len(argv) == 1:
            help()

        for node in configs['slaves']:
            print 'Processing %s...' % node
            cmd_str = ' '.join(argv[1:])
            common.auto_passwd('ssh -t %s@%s "%s"' % (configs['username'], 
                node, cmd_str), configs['password'])
        return 0
