from setuptools import setup, find_packages

setup(
    name='dokuwiki-https',
    version='0.5.0',
    author='Nicholas Biancolin',
    author_email='n.biancolin@mail.utoronto.ca',
    description='A higher-level API to interface with a dokuwiki over raw HTTPS (aka. without the security risk from XML-RPC)',
    packages=find_packages(),
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)