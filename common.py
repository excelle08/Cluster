import imp, os, json, pexpect
from modules import Command
from inspect import isclass


# Inherit the built in dict and list to make it support weak reference
class Dict(dict):
    pass


class List(list):
    pass


def load_class_from_file(path):
    mod_name, ext = os.path.splitext(os.path.split(path)[-1])
    py_mod = None
    classes = List()

    if ext.lower() == '.py':
        py_mod = imp.load_source(mod_name, path)
    elif ext.lower() == '.pyc':
        py_mod = imp.load_compiled(mod_name, path)

    if not py_mod:
        return []
    
    directives = dir(py_mod)
    for item in directives:
        c = getattr(py_mod, item)
        if item != 'Command' and isclass(c) and issubclass(c, Command):
            classes.append(c)

    return classes


def load_modules():
    files = os.listdir('./modules')
    classes = Dict()
    for filename in files:
        if filename.startswith('__'):
            continue
        if filename.endswith('.py'):
            class_list = load_class_from_file('./modules/%s' % filename)
            for c in class_list:
                classes[c().name()] = c
    return classes


def load_config():
    if not os.path.isfile('./clusters.conf'):
        return None

    config_str = ''
    with open('./clusters.conf', 'r') as f:
        config_str = f.read()
    return json.loads(config_str)


def auto_passwd(command, password):
    child = pexpect.spawn(command)
    
    while True:
        code = child.expect(['assword', pexpect.EOF, pexpect.TIMEOUT])
        if code == 0:
            child.sendline(password)
        else:
            break

