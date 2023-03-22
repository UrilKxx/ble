from abc import abstractmethod


class Storage(object):

    @abstractmethod
    def create_db(self):
        ...

    @abstractmethod
    def get_devices(self):
        ...

    @abstractmethod
    def add_device(self):
        ...

    @abstractmethod
    def update_device(self):
        ...

    @abstractmethod
    def update_online_device(self):
        ...

    @abstractmethod
    def delete_device(self):
        ...

    @abstractmethod
    def add_statistic_data(self):
        ...

    @abstractmethod
    def get_statistic_data(self):
        ...

