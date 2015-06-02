# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from http_errors.project import Project, ProjectPathError
from http_errors.config import ValidationError


def test_wrong_path(tmpdir):
    project_path = tmpdir.mkdir('dir')
    project = Project(str(project_path))
    project.create(force=True)
    with pytest.raises(ProjectPathError):
        project.create(force=False)


def test_wrong_config_file(tmpdir):
    project_path = tmpdir.mkdir('dir')
    project_path.join('project.ini').write('test')
    with pytest.raises(ValidationError):
        Project(str(project_path))


def test_project_load_templates(tmpdir):
    project_path = tmpdir.mkdir('dir')
    project = Project(str(project_path))
    project.create(force=True)
    project.load()
    assert len(project.get_templates()) == 2


def test_project_build(tmpdir):
    project_path = tmpdir.mkdir('dir')
    project = Project(str(project_path))
    project.create(force=True)
    project.load()
    assert project.build() is None
