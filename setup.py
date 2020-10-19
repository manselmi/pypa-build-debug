# stdlib imports
from pathlib import Path

# third-party imports
import Cython.Build
import setuptools


distribution_pkg_name = 'pypa-build-debug'
import_pkg_name = distribution_pkg_name.replace('-', '_')
pkg_dir = Path('src').joinpath(import_pkg_name)


ext_modules = Cython.Build.cythonize(
    module_list=[
        setuptools.Extension(
            name=f'{import_pkg_name}._primes',
            sources=[str(pkg_dir.joinpath('_primes.pyx'))],
        ),
    ],
    compiler_directives={
        'language_level': 3,
    },
)


setuptools.setup(
    author='Michael Anselmi',
    author_email='ma.anselmi@gmail.com',
    description='PyPA build debug',
    ext_modules=ext_modules,
    include_package_data=True,
    long_description=Path('README.rst').read_text(),
    long_description_content_type='text/x-rst',
    name=distribution_pkg_name,
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>= 3.6',
    url='https://github.com/manselmi/pypa-build-debug',
    zip_safe=False,
)
