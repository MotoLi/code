# coding: utf-8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': '尼达耶胶囊',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': '2098537060@qq.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)