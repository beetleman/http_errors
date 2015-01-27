# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class App:

    def __init__(self, argparser):
        """Main app class

        :param argparser: argparse.ArgumentParser
        """
        self.argparser = argparser
        self.project = None

    def run(self):
        """Run app"""
        args = self.argparser.parse_args()
