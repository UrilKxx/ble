import sqlite3 as sl
import time
from typing import List

from Device import Device
from Storage import Storage


class SQLiteStorage(Storage):

    def __int__(self, db: str):
        self._db = db

    def con_db(self, func):
        def wrapper(*args, **kwargs):
            try:
                con = sl.connect(self._db)
                print("connect to devices.db")
                value = func(con, *args, **kwargs)
                return value
            except Exception as e:
                print("some get wrong")
                return e
            finally:
                print("close connect to devices.db")
                con.close()

        return wrapper

    @con_db
    def create_db(self, connection):
        cursor = connection.cursor()
        query = '''
    create table devices
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
        data = cursor.execute("SELECT * FROM devices")
        for row in data:
            devices.append(Device(*row))
        return devices

    @con_db
    def add_device(self, connection, device: Device) -> Device:
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO devices (mac, avg_battery, avg_temp, avg_humidity, online) VALUES ('{device.mac}', {device.avg_battery}, {device.avg_temperature}, {device.avg_humidity}, {device.is_online})")
        connection.commit()
        return device

    @con_db
    def update_device(self, connection, device: Device) -> Device:
        cursor = connection.cursor()
        cursor.execute(
            f"UPDATE devices SET avg_battery = {device.avg_battery}, avg_temp = {device.avg_temperature}, avg_humidity = {device.avg_humidity}, online = {device.is_online} WHERE mac = '{device.mac}'")
        connection.commit()
        return device

    @con_db
    def update_online_device(self, connection, device: Device) -> Device:
        cursor = connection.cursor()
        cursor.execute(f"UPDATE devices SET online = {device.is_online} WHERE mac = '{device.mac}'")
        connection.commit()
        return device

    @con_db
    def delete_device(self, connection, device: Device):
        cursor = connection.cursor()
        cursor.execute(f"DELETE from devices WHERE mac = '{device.mac}'")
        connection.commit()

    @con_db
    def add_statistic_data(self, connection, mac: str, temperature: float = 0,
                           humidity: float = 0, battery: float = 0):
        cursor = connection.cursor()
        cursor.execute(
            f"INSERT INTO statistic_data (divice_mac, time, temperature, humidity, battery) VALUES ('{mac}', '{time.ctime()}', {temperature}, {humidity}, {battery})")
        connection.commit()

    @con_db
    def get_statistic_data(self, connection):
        statistic_data = []
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM statistic_data")
        for row in data:
            statistic_data.append(row)
        return statistic_data
