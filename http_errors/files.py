# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import os
import base64

import magic


class File(io.FileIO):
    mime = 'text/plain'
    __openmode = 'r'

    def __init__(self, file_path):
        """File

        :param file_path: file path
        """
        return super(File, self).__init__(
            file_path,
            self.__openmode
        )

    @property
    def file_name(self):
        return os.path.split(self.name)[1]

    def to_str(self):
        r = self.read()
        self.seek(0)
        return r


class JsFile(File):
    mime = 'text/javascript'

    def __init__(self, path, minimalize=False):
        super(JsFile, self).__init__(path)
        self.minimalize = minimalize


class CssFile(File):
    mime = 'text/css'

    def __init__(self, path, minimalize=False):
        super(CssFile, self).__init__(path)
        self.minimalize = minimalize


class ImageFile(File):
    magic = magic.Magic(mime=True)
    to_base64_template = 'data:{mime};base64,{data}'
    __openmode = 'rb'

    @property
    def mime(self):
        buffer = self.read(200)
        self.seek(0)
        return self.magic.from_buffer(buffer).decode('utf-8')

    def to_str(self):
        data = base64.b64encode(self.read()).decode('utf-8')
        self.seek(0)
        return self.to_base64_template.format(
            data=data,
            mime=self.mime
        )
