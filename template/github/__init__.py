import sys
import importlib.abc
import importlib.machinery

from .ghprocessor import get_github, create_base_url


def is_package(fullname):
    # Check if file.py exists


class GithubModuleFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, name, path, target=None):
        print('MyModuleFinder: Trying to load: {}'.format(name))

        # Don't import other modules

        return importlib.machinery.ModuleSpec(name, GithubLoader(), is_package=is_package(name))


class GithubLoader(importlib.abc.SourceLoader):
    def get_filename(self, fullname):
        print('MyLoader: Requesting filename for {}'.format(fullname))
        url = create_base_url(fullname)
        # If a package, return its __init__.py

        # Otherwise, return its .py file url


    def get_data(self, filename):
        print('MyLoader: Fetching {} from our virtual filesystem'.format(filename))
        # Workaround to simplify things
        if filename == 'http://github.com/FAKE/__init__.py':
            return ''

        # Get the file from Github


# Install module
sys.meta_path.insert(0, GithubModuleFinder())
