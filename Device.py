class Device(object):
    def __init__(self, mac: str, avg_battery: float = 0.0,
                 avg_temperature: float = 0.0,
                 avg_humidity: float = 0.0,
                 is_online: bool = False):
        self.mac: str = mac
        self.avg_battery: float = avg_battery
        self.avg_temperature: float = avg_temperature
        self.avg_humidity: float = avg_humidity
        self.is_online: bool = is_online

    def __str__(self):
        return "" + self.mac + " " + str(self.avg_temperature) + " " + str(self.avg_humidity) + " " + str(
            self.avg_battery) + " " + str(self.is_online)