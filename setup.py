
import os, sys
from setuptools import setup, find_packages
from setuptools.command.install import install as _install

scripts = [
    'dmm',
    'dmi',
    'dmindent',
    'dmmrender',
    'dmmfix',
    
    #TODO: Combine into dmi.
    'ss13_makeinhands',
    
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
    
setup(name='BYONDTools',
    version='0.1.1',
    description='Tools and interfaces for interacting with the BYOND game engine.',
    long_description = (read('README.rst') + '\n\n' +
                        read('CHANGELOG.rst')),# + '\n\n' +
                        #read('AUTHORS.rst'))
    url='http://github.com/N3X15/BYONDTools',
    author='N3X15',
    author_email='nexisentertainment@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'Pillow'
    ],
    tests_require=['unittest-xml-reporting'],
    test_suite='tests',
    scripts=scripts,
    zip_safe=False,
    cmdclass={'install': install}
)