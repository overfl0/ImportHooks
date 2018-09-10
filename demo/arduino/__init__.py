import importlib.abc
import importlib.machinery
import sys
import time

import serial

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
arduinos = list(filter(lambda device: device.pid == 32822 and device.vid == 9025, ports))
if not arduinos:
    raise RuntimeError('Could not find connected arduinos!')

print('Attempting connection to {}'.format(arduinos[0].device))
arduino = serial.Serial(arduinos[0].device, 115200, timeout=.1)


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

