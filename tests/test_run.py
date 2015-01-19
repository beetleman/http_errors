# -*- coding: utf-8 -*-
import subprocess


def test_run_main():
    assert subprocess.call(["http_errors", "-h"]) == 0
    assert subprocess.call(["http_errors", "--unknown option"]) == 2
