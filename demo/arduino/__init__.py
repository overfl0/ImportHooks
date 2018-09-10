import importlib.abc
import importlib.machinery
import sys
import time

from .helpers import connect_to_first_arduino_found

arduino = connect_to_first_arduino_found()


def get_filename(fullname):
    return 'arduino.py'


def is_package(fullname):
    return False


class MyImporter(importlib.abc.SourceLoader, importlib.abc.MetaPathFinder):
    def get_filename(self, fullname):
        print('MyImporter: Requesting filename for {}'.format(fullname))
        return get_filename(fullname)

    def get_data(self, filename):
        print('MyImporter: Reading data from Arduino'.format(filename))
        arduino.write(b'r')
        time.sleep(0.1)
        length = int(arduino.readline())
        print('MyImporter: The data will be {} bytes long...'.format(length))
        data = arduino.read(length)
        return data

    def find_spec(self, name, path, target=None):
        print('MyImporter: Trying to load: {}, path: {}, target: {}'.format(name, path, target))

        if not name.startswith('arduino.'):
            return False

        try:
            return importlib.machinery.ModuleSpec(name, self, is_package=is_package(name))

        except KeyError:
            return None


sys.meta_path.insert(0, MyImporter())
