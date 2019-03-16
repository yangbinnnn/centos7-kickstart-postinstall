import os
import sys


def log(msg, code=0):
    os.system('echo %s [%s]>> /tmp/postinstall.log' % (msg, code))
    if code != 0:
        sys.exit(code)

# sysconfig
code = os.system('cd sysconfig && python install.py')
if code == 0:
    log('install sysconfig success.')
else:
    log('install sysconfig fail.', code)

# install app
code = os.system('cd app && python install.py')
if code == 0:
    log('install app success.')
else:
    log('install app fail.', code)
