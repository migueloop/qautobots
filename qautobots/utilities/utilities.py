from __future__ import unicode_literals

import random
import string
import tempfile


def create_dummy_file(filename, size=1):
    """Create dummy file given filename and size"""
    tmpdir = tempfile.gettempdir()
    fpath = '{0}/{1}'.format(tmpdir, filename)
    f = open(fpath, 'w')
    f.seek(size)
    f.write('\0')
    f.close()
    return fpath


def random_string():
    """create random string"""
    return ''.join(random.choice(
        string.ascii_uppercase + string.digits) for _ in range(5))


def html_tag(tag, value=''):
    """Format given string to HTML tag"""
    return '<{0}>{1}</{0}>'.format(tag, value)
