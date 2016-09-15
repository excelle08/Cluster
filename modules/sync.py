from modules import Command
from cluster import configs
import common, os


class Sync(Command):
    """docstring for Cmd"""
    def __init__(self):
        super(Sync, self).__init__()

    def name(self):
        return 'sync'

    def intro(self):
        return 'Copy a file or directory to all slave machines'

    def help(self):
        return 'Usage: sync <PATH>'

    def execute(self, argv):
        if len(argv) == 1:
            help()

        path = argv[1]
        if not os.path.exists(path):
            print 'Path does not exist'
            return 1

        for node in configs['slaves']:
            print 'Processing node %s...' % node
            common.auto_passwd('rsync -a %s %s@%s:%s' % 
                (path, configs['username'], node, path), configs['password'])

        return 0
