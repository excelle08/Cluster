#!/usr/bin/python

import common
from sys import argv

if __name__ == '__main__':
    modules = common.load_modules()

    if len(argv) == 1:
        print 'Cluster Manager - A utility to manage Linux clusters.'
        print 'Usage: %s {SubCommands}\n' % argv[0]
        print 'Available commands:'
        for key, value in modules.iteritems():
            print '%s\t\t%s' % (key, value().intro())

        exit(0)

    module_name = argv[1]
    if not module_name in modules:
        print 'Subcommand %s is not implemented.' % module_name

    result = modules[module_name]().execute(argv[1:])
    exit(result)
