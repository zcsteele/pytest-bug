from m2r import parse_from_file
from setuptools import setup

import pytest_bug

setup(
    name='pytest-bug',
    description='pytest plugin for interaction with TestRail',
    long_description=parse_from_file('README.md'),
    version=pytest_bug.__version__,
    author='tolstislon',
    author_email='tolstislon@gmail.com',
    url='https://github.com/tolstislon/pytest-bug',
    packages=['pytest_bug'],
    install_requires=['pytest>=3.6.0'],
    include_package_data=True,
    python_requires='>=3.6',
    license='MIT License',
    entry_points={'pytest11': ['pytest_bug = pytest_bug.conftest']},
    keywords=['pytest'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Testing'
    ]
)
