# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import io
import magic
import base64


class Image(io.FileIO):
    magic = magic.Magic(mime=True)
    to_base64_template = 'data:{mime};base64,{data}'

    def __init__(self, file_path):
        """File

        :param file_path: file path
        """
        return super(Image, self).__init__(file_path, 'rb')

    def get_mime(self):
        buffer = self.read(200)
        self.seek(0)
        return self.magic.from_buffer(buffer).decode('utf-8')

    def get_base64(self):
        data = base64.b64encode(self.read()).decode('utf-8')
        self.seek(0)
        return self.to_base64_template.format(
            data=data,
            mime=self.get_mime()
        )
