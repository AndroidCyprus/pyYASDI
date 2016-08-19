import time

import pyYASDI
sma = pyYASDI.pyYASDI()

devices = sma.get_devices()
device = devices[0]
#name,sn,typ,channels = device.update_all()

def get_channel_handles(list):
    return [i.channel_handle for i in list]

def print_device(device):
    print("Device %s:"%(device.get_name()))
    print("handles:",get_channel_handles(device.channels))
    device.update_channels()
    print("handles:",get_channel_handles(device.channels))
    for n,i in enumerate(device.channels):
        print("({})".format(i.channel_handle))
        print("{}: ".format(n))
        name = i.update_name()
        print("{} = ".format(name))
        value = i.update_value()
        print("{}".format(value))
        unit = i.update_unit()
        print("{}".format(unit))
        """if n == 13:
            device.update_channels()
            time.sleep(1)
            #break
        """


for d in devices:
    print_device(d)
