from setuptools import find_packages
from setuptools import setup

setup(
    name='smartbot_controller',
    version='0.0.0',
    packages=find_packages(
        include=('smartbot_controller', 'smartbot_controller.*')),
)
