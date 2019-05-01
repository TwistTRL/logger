from distutils.core import setup

setup(
    name='logger',
    version='0.1.0',
    author='Lingyu Zhou',
    author_email='zhoulytwin@gmail.com',
    scripts=['bin/logger.py'],
    url='https://github.com/TwistTRL/logger',
    license='GPL-3.0',
    description='https://github.com/TwistTRL/logger',
    install_requires=[
        "docopt >= 0.6.1",
    ],
)
