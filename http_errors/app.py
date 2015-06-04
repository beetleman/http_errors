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

    def _check(self, project):
        errors = project.validate()
        for e in errors:
            print('error: %s' % e, file=sys.stderr)
        return len(errors) == 0

    def check(self, path, force):
        if force:
            print('`--force` option is useless whith `check`')
        project = Project(path)
        self._check(project)

    def build(self, path, force):
        project = Project(path)
        if not self._check(project):
            return
        project.build(force)

    def create(self, path, force):
        if force:
            project = Project(path, force)
        else:
            project = Project(path, force)
            project.create()
            project.load()
        if not self._check(project):
            return

    def run(self):
        '''Run app'''
        args = self.argparser.parse_args()
        getattr(self, args.command)(
            path=args.path,
            force=args.force
        )
