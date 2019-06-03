#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

import podcasts

setup(
    name="podcasts",
    version="0.0.2",
    packages=find_packages(),
    author="Jorrin Pollard",
    author_email="hi@jorr.in",
    description="Parse podcasts with Python",
    url="https://github.com/jorrinpollard/podcasts",
    long_description="README at https://github.com/jorrinpollard/podcasts",
    license="MIT",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    keywords=["podcasts"],
    install_requires=["xmljson"],
)
