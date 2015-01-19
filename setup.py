# -*- coding: utf-8 -*-

from setuptools import setup


requires = (
    'Jinja2'
)


setup(
    name="http_errors",
    version="0.0.1",
    author="Mateusz Probachta",
    author_email="mateusz.probachta@gmail.com",
    description=("Tool for generating static html for defined http erros"),
    license = "BSD",
    keywords = "generator http",
    url = "https://github.com/beetleman/http_codes",
    packages=['http_errors'],
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'http_errors = http_errors.run:main',
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
