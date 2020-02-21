from setuptools import setup, find_packages

version = {}
with open("src/randpin/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='randpin',
    version=version['__version__'],
    author='Andrei Vacariu',
    author_email='andrei@vacariu.ca',
    description='A simple tool for opening a random unread bookmark from Pinboard',
    url="https://github.com/avacariu/randpin",

    python_requires='>=3.5',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    entry_points={
        'console_scripts': [
            'randpin=randpin.__main__:main',
        ],
    },

    install_requires=[
        'click',
        'pinboard',
    ],

    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ]
)
