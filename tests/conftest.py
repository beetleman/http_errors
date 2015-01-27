# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import pytest

@pytest.fixture
def testfiles_path():
    return os.path.join(os.path.dirname(__file__), 'testfiles')
