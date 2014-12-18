#!/usr/bin/python

import sys

if len(sys.argv) == 2:
    userStr = sys.argv[1]
    hexPrefix=r'\x'
    print '\n' + '[+] Byte string:\n-------------------------------------------------------------------------\n' + r'\x' + hexPrefix.join(i.encode('hex') for i in userStr) + '\n-------------------------------------------------------------------------'

else:
        print '\nUsage: ' + str(sys.argv[0]) + ' [string to convert]\n'
        exit(0)
