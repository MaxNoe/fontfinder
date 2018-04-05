import sys
import subprocess as sp

if sys.platform != 'linux':
    raise NotImplementedError('Only linux is supported for now')

try:
    sp.check_output(['which', 'fc-list'])
except sp.CalledProcessError:
    raise OSError('This module only supports systems using "fontconfig"')
