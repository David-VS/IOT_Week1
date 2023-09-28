class Device:

    def __init__(self, name="default", is_on=False):
        self.name = name
        self.is_on = is_on

    def switch_off(self):
        self.is_on = False

    def switch_on(self):
        self.is_on = True

    def toggle(self):
        self.is_on = not self.is_on

    def __str__(self) -> str:
        return self.name + ", on: " + str(self.is_on)

    def __repr__(self):
        return self.__str__()
