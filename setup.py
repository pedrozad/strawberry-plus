#!/usr/bin/env python

from os import path, walk

import sys
from setuptools import setup, find_packages

NAME = "Strawberry Plus"
VERSION = "1.0"
AUTHOR = 'Diego Daniel Pedroza Perez'
AUTHOR_EMAIL = 'estuddiantep28@gmail.com'
URL = 'https://github.com/'
DESCRIPTION = "Strawberry Plus is a LOW-CODE metaheuristic algorithms tool, developed as an add-on to Orange Data Mining Framework"
#LONG_DESCRIPTION = open(path.join(path.dirname(__file__), 'README.pypi'),
#                        'r', encoding='utf-8').read()

LICENSE = "BSD"
KEYWORDS = (
    # [PyPi](https://pypi.python.org) packages with keyword "orange3 add-on"
    # can be installed using the Orange Add-on Manager
    'data mining',
    'machine learning',
    'artificial intelligence',
    'optimization',
    'metaheuristics',
    'orange3',
    'orange3 add-on',
)

PACKAGES = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

PACKAGE_DATA = {
    'StrawberryPlus.widgets': ['icons/*'],
}
DATA_FILES = [
    # Data files that will be installed outside site-packages folder
]

INSTALL_REQUIRES = [
    'Orange3',
    'jmetalpy'
]

ENTRY_POINTS = {
    # Entry points that marks this package as an orange add-on. If set, addon will
    # be shown in the add-ons manager even if not published on PyPi.
    'orange3.addon': (
        'StrawberryPlus = StrawberryPlus',
    ),
    # Entry point used to specify packages containing widgets.
    'orange.widgets': (
        # Syntax: category name = path.to.package.containing.widgets
        # Widget category specification can be seen in
        #    orangecontrib/example/widgets/__init__.py
        'Examples = orangecontrib.example.widgets',
        'StrawberryPlus Metaheuristics = StrawberryPlus.metaheuristics.widgets',
        'StrawberryPlus Sample Problems = StrawberryPlus.problems.widgets',
        'StrawberryPlus Utilities = StrawberryPlus.utilities.widgets',
    ),

    # Register widget help
    "orange.canvas.help": (
        'html-index = StrawberryPlus.widgets:WIDGET_HELP_PATH',)
}

NAMESPACE_PACKAGES = ["StrawberryPlus"]

TEST_SUITE = "StrawberryPlus.tests.suite"

def include_documentation(local_dir, install_dir):
    global DATA_FILES
    if 'bdist_wheel' in sys.argv and not path.exists(local_dir):
        print("Directory '{}' does not exist. "
              "Please build documentation before running bdist_wheel."
              .format(path.abspath(local_dir)))
        sys.exit(0)

    doc_files = []
    for dirpath, dirs, files in walk(local_dir):
        doc_files.append((dirpath.replace(local_dir, install_dir),
                          [path.join(dirpath, f) for f in files]))
    DATA_FILES.extend(doc_files)


if __name__ == '__main__':
    include_documentation('doc/_build/html', 'help/orange3-example')
    setup(
        name=NAME,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        description=DESCRIPTION,
        # long_description=LONG_DESCRIPTION,
        # long_description_content_type='text/markdown',
        license=LICENSE,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        data_files=DATA_FILES,
        install_requires=INSTALL_REQUIRES,
        entry_points=ENTRY_POINTS,
        keywords=KEYWORDS,
        namespace_packages=NAMESPACE_PACKAGES,
        zip_safe=False,
    )
