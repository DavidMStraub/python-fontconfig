# vim: set fileencoding=utf-8:
# @Name: setup.py
from distutils.core import setup
from distutils.extension import Extension

ext_modules = [
  Extension('fontconfig',
            ['fontconfig.c'],
            libraries=["fontconfig"])
]

setup(
  name='Font Config',
  version='0.2.0',
  author='Vayn a.k.a. VT',
  author_email='vayn@vayn.de',
  description='Python bindings for Fontconfig library',
  url='https://github.com/Vayn/python-fontconfig',
  ext_modules=ext_modules
)
