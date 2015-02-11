# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import shutil

from .config import Config
from .templete import ErrorTemplate


PROJECT_TEMPLATE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'project_template'
)


class ProjectError(Exception):
    pass


class ProjectPathError(ProjectError):
    pass


class Project:

    def __init__(self, project_path, force=False):
        self._project_path = project_path
        if self._is_project(project_path):
            self.load()
        else:
            self.create(force)
            self.load()

    def create(self, force=False):
        if os.path.isdir(self._project_path):
            if force is not False:
                raise ProjectPathError('%s exist.' % self._project_path)
            else:
                shutil.rmtree(self._project_path)
        return shutil.copytree(PROJECT_TEMPLATE_PATH, self._project_path)

    def build(self, force=True):
        for template in self.get_templates():
            file_path = self._path_join(
                self._config.general.output,
                template.output_filename
            )
            if os.path.exists(file_path) and force is False:
                raise ProjectPathError('%s exist.' % self._project_path)
            else:
                os.remove(file_path)
            with open(file_path) as fp:
                fp.write(template.render())

    def get_templates(self):
        templates = []
        templates_dir = self._config.general.templates_dir
        for error in self._config.general.errors:
            for code in error.codes:
                template = ErrorTemplate(
                    templates_dir=templates_dir,
                    name=error.template_file_path
                )
                template.code = code
                self._add_images(template)
                self._add_css(template)
                self._add_css(template)
                templates.append(template)
        return templates

    def _add_file(self, template, path, method, **kwargs):
        for file_name in self._path_join(path):
            getattr(template, method)(self._path_join(
                path, file_name, **kwargs))

    def _add_images(self, template):
        self._add_file(
            template,
            self._config.images.path,
            'add_image'
        )

    def _add_css(self, template, path):
        self._add_file(
            template,
            self._config.css.path,
            'add_css',
            minimalize=self._config.css.minimalize
        )

    def _add_js(self, template, path):
        self._add_file(
            template,
            self._config.js.path,
            'add_js',
            minimalize=self._config.js.minimalize
        )

    def load(self):
        config = Config(self._path_join('project.ini'))
        config.parse()
        config.validate()
        self._config = config

    def _is_project(self, path):
        return os.path.isdir(path) and os.path.isfile(
            self._path_join('project.ini'))

    def _path_join(self, *path):
        return os.path.join(self._project_path, *path)

    def validate(self):
        # TODO: check all folders and dirs from self._config
        pass
