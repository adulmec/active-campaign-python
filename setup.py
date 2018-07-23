#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
finally:
    import os

readme = open("README.md").read() if os.path.isfile("README.md") else ""

requirements = [
    'requests'
]

test_requirements = [
    # none yet
]

setup(
    name='active-campaign-python',
    version='0.9.2',
    description="Python ActiveCampaign API client",
    long_description=readme,
    author="Dennis Durling",
    author_email='djdtahoe@gmail.com',
    url='https://github.com/tahoe/active-campaign-python',
    packages=['activecampaign', ],
    package_dir={'activecampaign': 'activecampaign'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='activecampaign',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
