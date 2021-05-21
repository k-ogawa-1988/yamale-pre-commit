from setuptools import find_packages
from setuptools import setup


setup(
    name='pre-commit-yamale',
    description='Pre-commit hooks for Yamale',
    url='https://github.com/k-ogawa-1988/pre-commit-yamale',
    version='0.0.1',

    author='Contributors',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'pre-commit~=2.12',
        'yamale~=3.0',
    ],
    python_requires='>=3.6.1',
    entry_points={
        'console_scripts': [
            'yamale-validate = pre_commit_hooks.yamale_validate:main',
        ],
    },
)
