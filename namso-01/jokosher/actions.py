#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# if pisi can't find source directory, see /var/pisi/jokosher/work/ and:
# WorkDir="jokosher-"+ get.srcVERSION() +"/sub_project_dir/"

shelltools.export("HOME", get.workDIR())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("jokosher")

# You can use these as variables, they will replace GUI values before build.
# Package Name : jokosher
# Version : 0.11.5
# Summary : A simple yet powerful multi-track studio

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
