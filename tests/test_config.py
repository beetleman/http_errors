# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from http_errors.config import Config


def test_config(project_template_path):
    config = Config(os.path.join(project_template_path, 'project.ini'))
    assert config.parse() is None
    assert config.validate() is None
    assert len(config.general.errors) == 1
    assert len(config.general.errors[0].codes) == 2
