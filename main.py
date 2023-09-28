from classes import devicemanager as dm
from classes import device as d

manager = dm.DeviceManager()
lamp1 = d.Device("Philips hue", True)

manager.add_device(124, lamp1)

print(manager)
