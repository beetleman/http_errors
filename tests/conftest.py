# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import pytest


@pytest.fixture
def root_path():
    return os.path.dirname(os.path.dirname(__file__))


@pytest.fixture
def testfiles_path():
    return os.path.join(os.path.dirname(__file__), 'testfiles')


@pytest.fixture
def project_template_path(root_path):
    return os.path.join(root_path, 'http_errors', 'project_template')
