# -*- coding: utf-8 -*-
from __future__ import unicode_literals


try:
    from configparser import ConfigParser
    from configparser import Error as ParserError
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser
    from ConfigParser import Error as ParserError


class ValidationError(Exception):
    pass


class ConfigPart(object):

    def validate(self):
        pass


class FilePathConfigPart(ConfigPart):
    file_path = None

    def validate(self):
        super(FilePathConfigPart, self).validate()
        if self.file_path is None:
            raise ValidationError()


class JsConfigPart(FilePathConfigPart):
    minimalize = False


class CssConfigPart(FilePathConfigPart):
    minimalize = False


class ImagesConfigPart(FilePathConfigPart):
    pass


class ErrorConfigPart(ConfigPart):
    template_file_path = None

    def __init__(self):
        self.codes = []

    def validation(self):
        super(ErrorConfigPart, self).validation()
        if len(self.codes) == 0 or self.template_file_path is None:
            raise ValidationError()


class GeneralConfigPart(ConfigPart):
    output = None

    def __init__(self):
        self.errors = []

    def validation(self):
        super(GeneralConfigPart, self).validation()
        if len(self.errors) == 0 or self.output is None:
            raise ValidationError()
        for err in self.errors:
            err.validate()


class Config:
    images = ImagesConfigPart()
    js = JsConfigPart()
    css = CssConfigPart()
    general = GeneralConfigPart()

    def __init__(self, conf_path):
        self._config = ConfigParser()
        if conf_path not in self._config.read([conf_path]):
            raise ValidationError()

    def validate(self):
        self.images.validate()
        self.js.validate()
        self.css.validate()
        self.general.validate()

    def _parse_file_path(self, obj, section, option):
        try:
            obj.file_path = self._config.get(section, option)
        except ParserError:
            pass

    def parse_images(self):
        self._parse_file_path(self.images, 'images', 'path')

    def parse_js(self):
        self._parse_file_path(self.js, 'js', 'path')

    def parse_css(self):
        self._parse_file_path(self.css, 'css', 'path')

    def _parse_errors(self, section):
        error = ErrorConfigPart()
        try:
            error.template_file_path = self._config.get(section, 'template')
            error.codes.extend(self._config.get(section, 'codes').split())
        except ParserError:
            pass
        finally:
            self.general.errors.append(error)

    def parse_general(self):
        try:
            self.general.output = self._config.get('general', 'output')
            map(self._parse_errors,
                self._config.get('general', 'errors').split())
        except ParserError:
            pass

    def parse(self):
        self.parse_images()
        self.parse_js()
        self.parse_css()
        self.parse_general()
