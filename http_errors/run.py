# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import argparse
import sys


from .app import App


def run(argparser):
    app = App(argparser)
    app.run()


def main():
    argparser = argparse.ArgumentParser(sys.argv[0])
    run(argparser)


if __name__ == '__main__':
    main()
