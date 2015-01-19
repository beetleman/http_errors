# -*- coding: utf-8 -*-
import subprocess
import pytest

from http_errors import run


def test_script():
    assert subprocess.call(["http_errors", "-h"]) == 0
    assert subprocess.call(["http_errors", "--unknown option"]) == 2


def test_main():
    with pytest.raises(TypeError):
        run.run()
