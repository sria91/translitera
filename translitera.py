#!/usr/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'translitera','console_scripts','translitera'
__requires__ = 'translitera'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('translitera', 'console_scripts', 'translitera')(sys.argv)
    )
