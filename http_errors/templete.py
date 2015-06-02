# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jinja2 import Environment, FileSystemLoader

from http_errors.files import ImageFile, CssFile, JsFile


class DictTagFactory(object):

    def __init__(self, obj_dict):
        self._obj_dict = obj_dict

    def get_content(self, name):
        return self._obj_dict[name]

    def __call__(self, name):
        return self.get_content(name)


class FileTagFactory(DictTagFactory):

    def get_content(self, name):
        return super(FileTagFactory, self).get_content(name).to_str()


class ErrorTemplate:
    code = None
    _name = None

    def __init__(self, templates_dir, name):
        self._template_env = Environment(
            loader=FileSystemLoader(templates_dir)
        )
        self._name = name
        self._css_dict = {}
        self._images_dict = {}
        self._js_dict = {}

    @property
    def output_filename(self):
        return '%s.html' % self.code

    def get_template(self):
        return self._template_env.get_template(self._name)

    def render(self):
        context = {}
        self.update_context(context)
        self._template_env.filters['css'] = FileTagFactory(self._css_dict)
        self._template_env.filters['js'] = FileTagFactory(self._js_dict)
        self._template_env.filters['image'] = FileTagFactory(self._images_dict)

        template = self.get_template()
        return template.render(**context)

    def update_context(self, context):
        context['code'] = self.code

    def add_css(self, css_path, minimalize=False):
        css = CssFile(css_path, minimalize)
        self._css_dict[css.file_name] = css

    def get_template_tags(self):
        tags = {}
        return tags

    def add_js(self, js_path, minimalize=False):
        js = JsFile(js_path, minimalize)
        self._js_dict[js.file_name] = js

    def add_image(self, image_path):
        image = ImageFile(image_path)
        self._images_dict[image.file_name] = image
