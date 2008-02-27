#!/usr/bin/python

NSPR_CO_TAG = 'NSPR_4_7_1_BETA1'
NSS_CO_TAG  = 'NSS_3_12_BETA2'
CORE_CO_TAG = 'HEAD'

NSPR_DIRS = ('nsprpub',)
NSS_DIRS  = ('dbm',
             'security/nss',
             'security/coreconf',
             'security/dbm')
CORE_DIRS = ('extensions/xmlextras',)

import os
import sys
from optparse import OptionParser

topsrcdir = os.getcwd()
if topsrcdir == '':
    topsrcdir = '.'

try:
    from subprocess import check_call
except ImportError:
    import subprocess
    def check_call(*popenargs, **kwargs):
        retcode = subprocess.call(*popenargs, **kwargs)
        if retcode:
            cmd = kwargs.get("args")
            if cmd is None:
                cmd = popenargs[0]
                raise Exception("Command '%s' returned non-zero exit status %i" % (cmd, retcode))

def check_call_noisy(cmd, *args, **kwargs):
    print "Executing command:", cmd
    check_call(cmd, *args, **kwargs)

def do_cvs_checkout(modules, tag, cvsroot, cvs):
    """Check out a CVS directory.
    modules is a list of directories to check out, e.g. ['nsprpub']
    """
    for module in modules:
        (parent, leaf) = os.path.split(module)
        check_call_noisy([cvs, '-d', cvsroot,
                          'checkout', '-P', '-r', tag, '-d', leaf,
                          'mozilla/%s' % module],
                         cwd=os.path.join(topsrcdir, parent))

o = OptionParser(usage="client.py [options] checkout")
o.add_option("--cvs", dest="cvs", default=os.environ.get('CVS', 'cvs'),
             help="The location of the cvs binary")
o.add_option("--cvsroot", dest="cvsroot",
             default=os.environ.get('CVSROOT', ':pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot'),
             help="The CVSROOT (default: :pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot")


try:
    (options, (action,)) = o.parse_args()
except ValueError:
    o.print_help()
    sys.exit(2)

if action in ('checkout', 'co'):
    do_cvs_checkout(CORE_DIRS, CORE_CO_TAG, options.cvsroot, options.cvs)
    do_cvs_checkout(NSPR_DIRS, NSPR_CO_TAG, options.cvsroot, options.cvs)
    do_cvs_checkout(NSS_DIRS, NSS_CO_TAG, options.cvsroot, options.cvs)
else:
    o.print_help()
    sys.exit(2)
