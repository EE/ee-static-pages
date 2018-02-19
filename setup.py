from setuptools import setup

setup(
    name='ee-static-pages',
    version='0.1',
    description='Django app which provides static pages functionality.',
    author='Laboratorium EE',
    packages=['ee_static_pages'],
    install_requires=[
        'django>=1.11.*',
        'commonmark>=0.7.*',
        'django-markwhat>=1.6.*'
    ],
    dependency_links=['https://github.com/EE/ee-seo-mixin/tarball/master#egg=ee-seo-mixin'],
)
