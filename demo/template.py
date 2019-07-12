import sys
import importlib.abc
import importlib.machinery


# This is our "virtual filesystem" for the sake of the demo, however you can
# store yor files wherever you want: on remote drives, in databases, even on
# your little arduino. Just modify `get_data()`
##### REPLACE FROM HERE #####
data = {
    'custom_module/__init__.py': b'''print('Executing custom_module.__init__.py')'''
}
########## TO HERE ##########


class MyImporter(importlib.abc.SourceLoader, importlib.abc.MetaPathFinder):
    def get_filename(self, fullname):
        """
        Get a virtual file name for the module to import. Its only use is to be passed to `get_data()` later, so you can
        return whatever you want here, as long as you're prepared to handle that in `get_data()`.
        :param fullname: the module name to load, for example: "stackoverflow.quicksort"
        :return: The "file name" that contains the code of the requested module. This will be passed to `get_data()` later
        """
        print('MyImporter: Requesting filename for {}'.format(fullname))
        ##### REPLACE FROM HERE #####
        path_name = fullname.replace('.', '/')

        if path_name + '/__init__.py' in data:
            return path_name + '/__init__.py'
        if path_name + '.py' in data:
            return path_name + '.py'
        ########## TO HERE ##########

        raise KeyError('{} not found'.format(fullname))

    def get_data(self, filename):
        """
        Return the actual code to be executed
        :param filename: Whatever you previously returned from get_filename will end up here
        :return: `b"print('Hello world from my module!')"` for example
        """
        ##### REPLACE FROM HERE #####
        print('MyImporter: Fetching {} from our virtual filesystem'.format(filename))
        return data[filename]
        ########## TO HERE ##########

    def is_package(self, fullname):
        """
        Is the fullname of the module a package or just a module.
        Hint: `something.py` is usually the `something` module
              `foo` directory containing `__init__.py` is usually the `foo` package.
        :param fullname: the module name to load, for example: "stackoverflow.quicksort"
        :return: True or False
        """
        ##### REPLACE FROM HERE #####
        return self.get_filename(fullname).endswith('/__init__.py')
        ########## TO HERE ##########

    def find_spec(self, name, path, target=None):
        """
        Decide whether it's our custom module that python wants to import or not.
        If it's not, return None to let python handle it
        :param name: the module name to load, for example: "stackoverflow.quicksort"
        :return: None if we don't want to handle that module. ModuleSpec otherwise.
        """
        print('MyImporter: Trying to load: {}, path: {}, target: {}'.format(name, path, target))

        ##### REPLACE FROM HERE #####
        # Only import "our" modules. Otherwise, return None to let python handle them
        if not name.startswith('custom_module'):
            return None
        ########## TO HERE ##########

        try:
            return importlib.machinery.ModuleSpec(name, self, is_package=self.is_package(name))

        except KeyError:
            return None


if __name__ == '__main__':
    # Install the importer.
    sys.meta_path.insert(0, MyImporter())

    import custom_module
