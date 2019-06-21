from setuptools import setup

setup(
    name='Alfred',
    version='Beta',
    author='Ayushman Dubey',
    author_email='dubeyayushmanrobin@protonmail.com',
    description='Beginner Pentesting Toolkit/Framework',
    url='https://github.com/d4mianwayne/Alfred',
    packages=['alfred'],
    install_requires=[
        'termcolor',
        'PyPDF2',
        'terminaltables',
        'pyfiglet',
        'requests',
    ],
    project_urls={
        'Wiki': 'https://github.com/d4mianwayne/Alfred/wiki',
    },
    license='GNU General Public License v3 (GPLv3) (GPL)',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'Alfred = alfred.__main__:main',
        ]
    })
