#!/usr/bin/python
# -*- coding: utf-8 -*-
#

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.system("./autogen.sh --disable-schemas-compile                \
                                    --disable-scrollkeeper                   \
                                    --disable-static                         \
                                    --prefix=/usr                            \
                                    --sysconfdir=/etc                        \
                                    --with-x                                 \
                                    --enable-polkit                          \
                                    --enable-networkmanager                  \
                                    --enable-ipv6                            \
                                    --disable-timer-applet                   \
                                    --libexecdir=/usr/libs/mate-applets ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "NEWS", "ChangeLog", "AUTHORS", "COPYING")