"""PyAsy setup script."""

import glob
import os
import re

try:
    from setuptools import setup
except:
    from distutils.core import setup


######################################################################
# version
version = '0.3.0'

######################################################################
# save git version to 'pyasy/__git_version__.py'

try:
    git_head_file = os.path.join(os.path.dirname(__file__), '.git', 'HEAD')
    f = open(git_head_file)
    m = re.match(r'ref: (.+)', f.readline())
    ref = m.group(1)
    f.close()

    git_head_file = os.path.join(os.path.dirname(__file__), '.git', ref)
    f = open(git_head_file)
    git_version = f.readline().rstrip()
    f.close()

except:
    git_version = 'not_available'

git_version_file = os.path.join(os.path.dirname(__file__),
                                'pyasy','__git_version__.py')
f = open(git_version_file, 'w')
f.write("version = '%s'\n" % (git_version))
f.close()


######################################################################
# save version to 'pyasy/__version__.py'

version_file = os.path.join(os.path.dirname(__file__),
                            'pyasy','__version__.py')
f = open(version_file, 'w')
f.write("version = '%s'\n" % (version))
f.close()


######################################################################
# setup!

setup(

    name = "PyAsy",
    version = version,
    packages = ['pyasy'],
    zip_safe = False,

    package_data = {'': ['__version__.py', '__git_version__.py']},
    exclude_package_data = {'': ['.gitignore']},

    author = "Matthew Emmett",
    author_email = "matthew.emmett@ualberta.ca",
    description = "PyAsy is a Python wrapper of the Asymptote vector graphics language.",
    license = "BSD",
    keywords = "vector, graphics, asymptote",
    url = "http://github.com/memmett/PyAsy"

    )
