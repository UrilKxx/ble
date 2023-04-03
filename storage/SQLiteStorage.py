import os
import sqlite3 as sl
import time
from typing import List

from logger import logger as logger

from storage.Device import Device
from storage.Storage import Storage

logger = logger.get_logger(__name__)


def con_db(func):
    def wrapper(*args, **kwargs):
        con = None
        db = args[0].db
        try:
            con = sl.connect(db)
            logger.info("Connect to " + db)
            value = func(*args, connection=con, **kwargs)
            return value
        except Exception as e:
            logger.error(f"Error connecting to database {db}: {str(e)}")
            return e
        finally:
            logger.info("Close connect to " + db)
            con.close()

    return wrapper


class SQLiteStorage(Storage):

    def __init__(self, db: str = 'devices.db'):
        self._db = db
        # if self._db not in os.listdir():
        #     self.create_db()

    @property
    def db(self) -> str:
        return self._db

    @con_db
    def create_db(self, connection):
        cursor = connection.cursor()
        query = '''
    create table 'devices'
    (
        mac text not null unique unique,
        avg_battery REAL default 0,
        avg_temp     REAL    default 0,
        avg_humidity REAL    default 0,
        online       INTEGER default 0 not null
    );

    create table statistic_data
    (
        divice_mac  TEXT not null
            constraint statistic_data_devices_mac_fk
                references devices (mac),
        time        TEXT not null,
        temperature REAL not null,
        humidity    real not null,
        battery     REAL not null
    );

    create unique index statistic_data_divice_mac_uindex
        on statistic_data (divice_mac);

        '''
        cursor.execute(query)

    @con_db
    def get_devices(self, connection) -> List[Device]:
        devices = []
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM 'devices'")
        for row in data:
            devices.append(Device(*row))
        return devices

    @con_db
    def get_device(self, mac: str, connection) -> Device:
        cursor = connection.cursor()
        data = cursor.execute(f"SELECT * FROM 'devices' WHERE mac = '{mac}'")
        return Device(*data[0])

    @con_db
    def add_device(self, mac: str, connection) -> Device:
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO 'devices' (mac) VALUES ('{mac}')")
        connection.commit()
        return self.get_device(mac)

    @con_db
    def update_device(self, device: Device, connection) -> Device:
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE 'devices' SET avg_battery = {device.avg_battery}, avg_temp = {device.avg_temperature}, avg_humidity = {device.avg_humidity}, online = {device.is_online} WHERE mac = '{device.mac}'")
        connection.commit()
        return device

    @con_db
    def update_online_device(self, device: Device, connection) -> Device:
        cursor = connection.cursor()
        cursor.execute(f"UPDATE 'devices' SET online = {device.is_online} WHERE mac = '{device.mac}'")
        connection.commit()
        return device

    @con_db
    def delete_device(self, device: Device, connection):
        cursor = connection.cursor()
        cursor.execute(f"DELETE from 'devices' WHERE mac = '{device.mac}'")
        connection.commit()

    @con_db
    def add_statistic_data(self, mac: str, temperature: float = 0,
                           humidity: float = 0, battery: float = 0, connection=None):
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO 'statistic_data' (divice_mac, time, temperature, humidity, battery) VALUES ('{mac}', '{time.ctime()}', {temperature}, {humidity}, {battery})")
        connection.commit()

    @con_db
    def get_statistic_data(self, connection):
        statistic_data = []
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM 'statistic_data'")
        for row in data:
            statistic_data.append(row)
        return statistic_data
