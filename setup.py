from setuptools import setup, find_packages
import dcusb

setup(
    name = 'dcusb',
    version = dcusb.__version__,
    packages = find_packages(),
    long_description=open('README.rst', 'rt').read(),
    install_requires = ['pyusb'],
    author = 'Chris Grice',
    author_email = 'chris@chrisgrice.com',
    license = 'MIT',
    description = 'Driver for DreamCheeky LED message board',
    url='http://github.com/cgrice/dcusb/',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
    ],
    zip_safe = False,
)