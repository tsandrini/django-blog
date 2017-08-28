#!/usr/bin/env python
from distutils.core import setup

version = __import__('blog').get_version()


setup(
    name='django-blog',
    version=version,
    description='Blog module',
    long_description=(),
    author='Tomáš Sandrini',
    author_email='tomas.sandrini@seznam.cz',
    maintainer='Tomáš Sandrini',
    maintainer_email='tomas.sandrini@seznam.cz',
    url='https://github.com/tsandrini/django-blog',
    packages=['blog'],
    package_data={'blog': ['static/blog/css/**/*.css',
                            'static/blog/js/**/*.js']},
    requires=['Django(>=1.8)'],
    download_url='https://github.com/tsandrini/django-blog/archive/%s.tar.gz' % version,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: MIT'],
license='MIT')
