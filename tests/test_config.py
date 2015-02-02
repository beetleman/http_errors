# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import pytest

from http_errors.config import Config


@pytest.fixture
def config(project_template_path):
    return Config(os.path.join(project_template_path, 'project.ini'))


def test_config(config):
    assert config.parse() is None
    assert config.validate() is None
