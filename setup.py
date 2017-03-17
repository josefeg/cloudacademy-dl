from setuptools import setup

import os
import subprocess

from cloudacademy import __version__


def read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except IOError:
        return ''


def generate_long_description():
    temp_file = 'temp.rst'
    cmd = [
        'pandoc',
        '--from=markdown',
        '--to=rst',
        '--output=' + temp_file,
        'README.md'
    ]

    long_description = ''
    try:
        subprocess.call(cmd)
        long_description = read_file(temp_file)
        os.remove(temp_file)
    except (IOError, OSError):
        long_description = 'Could not generate docs. Refer to README.md'

    return long_description


setup(
    name='cloudacademy-dl',
    version=__version__,
    author='Josef Galea',
    author_email='josefeg@gmail.com',

    license='MIT',
    url='https://github.com/josefeg/cloudacademy-dl',

    install_requires=[
        'beautifulsoup4>=4.5.3',
        'docopt>=0.6.2',
        'lxml>=3.6.0',
        'requests>=2.9.1'
    ],

    description='A utility for downloading CloudAcademy.com lecture videos.',
    long_description=generate_long_description(),
    keywords=[
        'cloudacademy-dl',
        'cloudacademy',
        'download',
        'education',
        'MOOCs',
        'video'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Education',
    ],

    packages=['cloudacademy'],
    entry_points=dict(
        console_scripts={
            'cloudacademy-dl=cloudacademy.cloudacademy_dl:main'
        }
    ),

    platforms=['any']
)
