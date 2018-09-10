import serial.tools.list_ports


def get_connected_arduinos():
    arduino_vids = [
        9025,  # Original Arduino
        6790,  # CH340 - based USB-serial clones
    ]

    ports = serial.tools.list_ports.comports()
    arduinos = list(filter(lambda device: device.vid in arduino_vids, ports))

    return arduinos


def connect_to_first_arduino_found(baudrate=115200):
    arduinos = get_connected_arduinos()

    if not arduinos:
        raise RuntimeError('Could not find connected arduinos!')

    print('Attempting connection to {}'.format(arduinos[0].device))
    arduino = serial.Serial(arduinos[0].device, baudrate, timeout=.1)

    return arduino
