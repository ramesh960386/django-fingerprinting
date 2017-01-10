# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='django-fingerprinting',
    version='1.0.1',
    keywords='django staticfiles',
    author=u'Sheepsy90 <sheepsy90@gmail.com>',
    packages=['django_fingerprinting'],
    url='https://github.com/sheepsy90/django-fingerprinting',
    license='see LICENCE',
    description='Replace names of static files and resources that are accessed from templates',
    requires=[
        'Django',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ]
)
