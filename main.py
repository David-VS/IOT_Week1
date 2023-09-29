from functions import math_utils as mu
from classes import devicemanager as dm
from classes import device as d


print(mu.fibonacci(3))
print(mu.highest_number(1, 2))
print(mu.highest_number(101, 2, 42, 56, 12))
print(mu.factorial(6))


manager = dm.DeviceManager()
lamp1 = d.Device("Philips hue", True)

manager.add_device(124, lamp1)

print(manager)
