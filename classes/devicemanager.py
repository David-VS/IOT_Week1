from classes import device

class DeviceManager:
    #composition, gebruik klassen binnen andere klasse
    device_dict = {}

    def __init__(self) :
        pass

    def add_device(self, _id, _device):
        self.device_dict[_id] = _device

    def remove_device(self, _id):
        self.device_dict.pop(_id)
        #alternatief
        #del self.device_dict[_id]

    def switch_everything_on(self):
        for _id in self.device_dict:
            _device = self.device_dict[_id]
            _device.switch_on()

    def switch_everything_off(self):
        for _id in self.device_dict:
            _device = self.device_dict[_id]
            _device.switch_off()

    def toggle_everything(self):
        for _id in self.device_dict:
            _device = self.device_dict[_id]
            if _device.is_on:
                _device.switch_off()
            else:
                _device.switch_on()

    def __str__(self):
        return self.device_dict.__str__()
