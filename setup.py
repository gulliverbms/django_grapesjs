import codecs
import os
import re
from distutils.core import setup
from setuptools import find_packages

try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = None


def read(*parts):
    """Read all data from a particular file."""
    with codecs.open(os.path.join(base_dir, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    """Find version of the particular package."""
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django_grapesjs',
    packages=find_packages(exclude=('example*',)),
    include_package_data=True,
    version=find_version('djang_grapesjs', '__about__.py'),
    description='A small library for integrating the page builder "grapesjs" into django admin',
    author='Mark Burkut',
    author_email='burkut888mark@gmail.com',
    url='https://github.com/gulliverbms/django_grapesjs',
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    keywords=['page builder'],
    classifiers=[
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Environment :: Web Environment",
    ],
    license='MIT',
    install_requires=read('requirements/prod.txt'),
)
