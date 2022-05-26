from setuptools import find_packages
from setuptools import setup


setup(
    name='yamale-pre-commit',
    description='Pre-commit hooks for Yamale',
    url='https://github.com/k-ogawa-1988/yamale-pre-commit',
    version='0.0.2',
    author='Contributors',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'envsubst~=0.1.5',
        'yamale~=3.0',
    ],
    python_requires='>=3.6.1',
    entry_points={
        'console_scripts': [
            'yamale-validate = yamale_validate.yamale_validate:main',
        ],
    },
)
