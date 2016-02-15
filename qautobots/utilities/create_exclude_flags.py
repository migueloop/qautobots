from __future__ import unicode_literals

import os
import sys

from qautobots.framework.qanfig import get_config


def main(argv, config):
    filename = argv
    decepticons = config

    if os.path.isfile(filename):
        os.remove(filename)

    with open(filename, 'w') as f:  # pragma: no cover
        for (dflag, value) in decepticons['decepticons'].items():
            if value:
                f.write('qautobots/tests/' + dflag + '\n')

if __name__ == '__main__':  # pragma: no cover
    main(sys.argv[1], get_config())
