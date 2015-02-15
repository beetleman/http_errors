# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mako.lookup import TemplateLookup

from http_errors.files import ImageFile, CssFile, JsFile


class ErrorTemplate:
    code = None
    _name = None

    def __init__(self, templates_dir, name):
        self._template_lookup = TemplateLookup(directories=[templates_dir])
        self._name = name
        self._css_list = {}
        self._images_list = {}
        self._js_list = {}

    @property
    def output_filename(self):
        return '%s.html' % self.code

    def get_template(self):
        return self._template_lookup.get_template(self._name)

    def render(self):
        context = {}
        template = self.get_template()
        self.update_context(context)
        return template.render(**context)

    def update_context(self, context):
        context['css'] = self._css_list
        context['js'] = self._js_list
        context['images'] = self._images_list
        context['code'] = self.code

    def add_css(self, css_path, minimalize=False):
        css = CssFile(css_path, minimalize)
        self._css_list[css.file_name] = css

    def add_js(self, js_path, minimalize=False):
        js = JsFile(js_path, minimalize)
        self._js_list[js.file_name] = js

    def add_image(self, image_path):
        image = ImageFile(image_path)
        self._images_list[image.file_name] = image
