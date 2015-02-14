# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from http_errors.project import Project, ProjectPathError
from http_errors.config import ValidationError


@pytest.fixture
def project(project_template_path):
    return Project(project_template_path)


def test_wrong_path(tmpdir):
    project_path = tmpdir.mkdir('dir')
    project_path.join('project.ini').write('test')
    with pytest.raises(ProjectPathError):
        Project(str(project_path), force=True)


def test_wrong_config_file(tmpdir):
    project_path = tmpdir.mkdir('dir')
    project_path.join('project.ini').write('test')
    with pytest.raises(ValidationError):
        Project(str(project_path))
