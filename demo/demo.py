import sys
import importlib.abc
import importlib.machinery


data = {
    'custom_module/__init__.py': b'''print('Executing intercept_modules.__init__.py')'''
}


def get_filename(fullname):
    path_name = fullname.replace('.', '/')

    if path_name + '/__init__.py' in data:
        return path_name + '/__init__.py'
    if path_name + '.py' in data:
        return path_name + '.py'

    raise KeyError('{} not found'.format(fullname))


def is_package(fullname):
    return get_filename(fullname).endswith('/__init__.py')


class MyImporter(importlib.abc.SourceLoader, importlib.abc.MetaPathFinder):
    def get_filename(self, fullname):
        print('MyImporter: Requesting filename for {}'.format(fullname))
        return get_filename(fullname)

    def get_data(self, filename):
        print('MyImporter: Fetching {} from our virtual filesystem'.format(filename))
        return data[filename]

    def find_spec(self, name, path, target=None):
        print('MyImporter: Trying to load: {}, path: {}, target: {}'.format(name, path, target))

        try:
            return importlib.machinery.ModuleSpec(name, self, is_package=is_package(name))

        except KeyError:
            return None


if __name__ == '__main__':
    # Install module
    sys.meta_path.insert(0, MyImporter())

import custom_module