import os, sys
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

scripts = [
    'dmm',
    'dmi',
    'dmi_compile',
    'dmindent',
    'dmmrender',
    'dmmfix',
    
    # Our post-install.  Now run on Linux, as well.
    "byondtools-postinstall"
]

def _post_install(_dir):
    '''Run our fancy post-install thing that builds batch files for windows.'''
    from subprocess import call
    #print('_dir={}'.format(_dir))
    call([sys.executable, 'byondtools-postinstall.py'], cwd=_dir)

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

class install(_install):
    def run(self):
        _install.run(self)
        # install_lib
        self.execute(_post_install, (self.install_scripts,),  msg="Running post install task")

options = {}
scripts = ['scripts/{}.py'.format(x) for x in scripts]
    
current_version='0.1.4'

setup(name='BYONDToolsv3',
    version=current_version,
    description='Tools and interfaces for interacting with the BYOND game engine, adapted to Python 3.',
    long_description = (read('README.rst') + '\n\n' +
                        read('CHANGELOG.rst') + '\n\n' +
                        read('AUTHORS.rst')),
    long_description_content_type = 'text/x-rst',
    url='https://github.com/ComicIronic/BYONDToolsv3',
    download_url='https://github.com/ComicIronic/BYONDToolsv3/tarball/v' + current_version,
    author='Comic',
    author_email='ivb@vanbakel.io',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    package_data = {'byond' : ['data/stdlib/*'] },
    install_requires=[
        'Pillow',
        'pyparsing',
        'numpy'
    ],
    tests_require=['unittest-xml-reporting'],
    test_suite='tests',
    scripts=scripts,
    zip_safe=True,
    cmdclass={'install': install}
)
