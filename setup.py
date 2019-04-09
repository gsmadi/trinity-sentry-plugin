#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='trinity-sentry-plugin',
    version='0.1.0',
    py_modules=['sentry_plugin'],
    entry_points={
        'trinity.plugins': 'sentry_plugin=sentry_plugin:SentryPlugin',
    },
    install_requires=[
        'sentry-sdk==0.7.9'
    ]
)