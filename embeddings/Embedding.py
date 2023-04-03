from typing import List

from bluepy.btle import Scanner

from storage.Device import Device
from scanner.ScanDelegate import ScanDelegate
from storage.SQLiteStorage import SQLiteStorage
from storage.Storage import Storage


# from bluepy.btle import BTLEException

class Embedding(object):
    def __init__(self, storage: Storage = SQLiteStorage(), timeout: int = 5):
        self._pollers = list()
        self._storage: Storage = storage
        self._timeout = timeout
        self._scanner = Scanner().withDelegate(ScanDelegate())

    # def check_devices(self):
    #     for d in self._storage.get_devices():
    #         self._pollers.append(MiTempBtPoller(d.mac, BluepyBackend, self._timeout))

    def scan_devices(self) -> List:
        devices = list()
        for d in self._scanner.scan():
            devices.append({"mac": d.addr, "type": d.addrType, "RSSI": d.rssi})
        return devices

    def add_device(self, mac) -> Device:
        return self._storage.add_device(mac)

    def get_devices(self) -> List:
        return self._storage.get_devices()

    def get_online_devices(self) -> List:
        # return self._storage.
        ...

    def get_device(self, mac) -> Device:
        return self._storage.get_device(mac)
