#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
APP_HOME = '/opt/myapp'
os.system('mkdir -p %s' % APP_HOME)
code = os.system('cp app.py %s' % APP_HOME)
if code == 0:
    print 'install success.'
else:
    print 'install fail.'
