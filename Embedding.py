from storage.SQLiteStorage import SQLiteStorage
from storage.Storage import Storage
from mitemp.mitemp_bt.mitemp_bt_poller import MiTempBtPoller
from mitemp.mitemp_bt.mitemp_bt_poller import MI_TEMPERATURE, MI_HUMIDITY, MI_BATTERY
from btlewrap.bluepy import BluepyBackend


# from bluepy.btle import BTLEException

class Embedding(object):
    def __int__(self, storage: Storage = SQLiteStorage('devices.db'), timeout: int = 5):
        self._pollers = list()
        self._storage: Storage = storage
        self._timeout = timeout
        self.make_pollers()

    def make_pollers(self):
        for d in self._storage.get_devices():
            self._pollers.append(MiTempBtPoller(d.mac, BluepyBackend, 5))
