# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mako.lookup import TemplateLookup

from http_errors.files import ImageFile, CssFile, JsFile


class ErrorTemplate:
    code = None
    template_file_name = None

    def __init__(self, templates_dir):
        self._template_lookup = TemplateLookup(directories=[templates_dir])
        self._csss = {}
        self._images = {}
        self._jss = {}

    def get_template(self):
        self._template_lookup.get_template(self.template_file_name)

    def render(self):
        context = {}
        template = self.get_template()
        self.update_context(context)
        return template.render(**context)

    def update_context(self, context):
        context['css'] = self._csss
        context['js'] = self._jss
        context['images'] = self._imagess
        context['code'] = self.code

    def add_css(self, css_path):
        css = CssFile(css_path)
        self._csss[css.file_name] = css

    def add_js(self, js_path):
        js = JsFile(js_path)
        self._jss[js.file_name] = js

    def add_image(self, image_path):
        image = ImageFile(image_path)
        self._images[image.file_name] = image
