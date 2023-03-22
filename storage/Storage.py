from abc import abstractmethod
from typing import List

from Device import Device


class Storage(object):

    @abstractmethod
    def create_db(self):
        ...

    @abstractmethod
    def get_devices(self) -> List[Device]:
        ...

    @abstractmethod
    def add_device(self, device: Device) -> Device:
        ...

    @abstractmethod
    def add_device(self, mac: str) -> Device:
        ...

    @abstractmethod
    def update_device(self, device: Device) -> Device:
        ...

    @abstractmethod
    def update_online_device(self, device: Device, online: bool) -> Device:
        ...

    @abstractmethod
    def delete_device(self, device: Device):
        ...

    @abstractmethod
    def add_statistic_data(self):
        ...

    @abstractmethod
    def get_statistic_data(self):
        ...
