# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import os
import sys

from .project import Project


class App:

    def __init__(self, argparser):
        """Main app class

        :param argparser: argparse.ArgumentParser
        """
        self.argparser = argparser
        self._init_argparser()
        self.project = None

    def _init_argparser(self):
        self.argparser.add_argument(
            'command',
            choices=['create', 'build', 'check']
        )
        self.argparser.add_argument(
            'path',
            default=os.getcwd()
        )
        self.argparser.add_argument(
            '--force',
            action='store_true',
            default=False
        )

    def check(self, path, force):
        if force:
            print('`--force` option is useless whith `check`')
        project = Project(path)
        errors = project.validate()
        for e in errors:
            print('error: %s' % e, file=sys.stderr)

    def build(self, path, force):
        print('build(self, path, force)', path, force)

    def create(self, path, force):
        print('create(self, path, force)', path, force)

    def run(self):
        '''Run app'''
        args = self.argparser.parse_args()
        getattr(self, args.command)(
            path=args.path,
            force=args.force
        )
