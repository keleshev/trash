#! /usr/bin/env python
import os, sys
from shutil import move
from datetime import datetime


def trash(*files, **options):
    if not files:
        exit('Usage: trash <files>...')
    assert list(options) in (['trash_dir'], [])
    trash_dir = os.path.expanduser(options.get('trash_dir') or '~/.Trash')
    timestamp = '.' + datetime.now().isoformat()
    for f in files:
        f = os.path.expanduser(f)
        to = os.path.join(trash_dir, f.split('/')[-1] + timestamp)
        print('%s -> %s' % (f, to))
        move(f, to)


if __name__ == '__main__':
    trash(*sys.argv[1:])
