# About
Simple flask API, which in background scans Xiaomi BLE Temperature and Humidity sensors and put in SQLite DB. 

| Specs                | []()                                                                                                                                                                                                                        |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temp/Humidity Sensor | SHT30-DIS-B (Typical accuracy of ±2% RH and ±0.2°C) [Datasheet](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/0_Datasheets/Humidity/Sensirion_Humidity_Sensors_SHT3x_Datasheet_digital.pdf) |
| SoC                  | N51802 (Nordic nRF51802)                                                                                                                                                                                                    |
| LCD Driver           | BU9795AFV [Datasheet](http://rohmfs.rohm.com/en/products/databook/datasheet/ic/driver/lcd_segment/bu9795afv-e.pdf)                                                                                                          |
| Power                | 1x AAA                                                                                                                                                                                                                      |

![Alt text](https://tehnoteca.ru/img/1737/1736245/xiaomi_mijia_hygrometer_bluetooth_1.jpg "Xiaomijia Bluetooth Temperature Smart Humi Dity Sensor Digital Thermometer Mi Home Battery")

***mitemp*** module based on [Xiaomi BLE Temperature and Humidity Sensor Bluetooth To MQTT gateway](https://github.com/algirdasc/xiaomi-ble-mqtt "GitHub")

# Installation (*Work just on linux*)
***Clone code***
```bash
git clone https://github.com/UrilKxx/ble.git
cd ble
```
***to make ble work***
```bash
sudo apt-get install libglib2.0-dev
```
## Install requirements packages
***From requirements.txt***
```bash
sudo pip3 install -r requirements.txt
```
***Terminal***
```bash
sudo pip3 install bluepy
sudo pip3 install btlewrap
sudo pip3 install logger
sudo pip3 install Flask
sudo pip3 install Flask-API
```
# Run
To view help run
```bash
 python3 main.py -h
```
```
usage: main.py [-h] [--kill_process_with_port KILL_PROCESS_WITH_PORT] [--port PORT]

ble args like port, kill process with port

options:
  -h, --help            show this help message and exit
  --kill_process_with_port KILL_PROCESS_WITH_PORT
                        provide an bool (default: True)
  --port PORT           provide an int port (default: 5000)
```
To start 
```bash
 python3 main.py 
```
To view device in DB
```http
http://host:5000 
```
```json
[
    {
        "mac": "4c:65:a8:da:a8:91",
        "avg_battery": 99.0,
        "avg_temperature": 27.791000000000025,
        "avg_humidity": 42.06300000000002,
        "is_online": 1
    }
]
```
To scan available devices
```http
http://host:5000/scan 
```
***All mac of this sensor start with __4C:65:A8:XX:XX:XX__***

```json
[
    {
        "RSSI": -82,
        "mac": "d7:c7:79:55:6e:e3",
        "type": "random"
    },
    {
        "RSSI": -92,
        "mac": "9c:8c:6e:0f:b8:68",
        "type": "public"
    },
    {
        "RSSI": -94,
        "mac": "77:ac:09:cd:67:9f",
        "type": "random"
    },
    {
        "RSSI": -52,
        "mac": "01:eb:29:c4:23:55",
        "type": "random"
    },
    {
        "RSSI": -50,
        "mac": "46:51:a9:91:77:e0",
        "type": "random"
    },
    {
        "RSSI": -60,
        "mac": "4c:65:a8:da:a8:91",
        "type": "public"
    }
]
```
To get device by ***mac***
```http
http://host:5000/devices/4C:65:A8:XX:XX:XX
```
```json
{
    "avg_battery": 99.0,
    "avg_humidity": 40.56953125000001,
    "avg_temperature": 27.84765625000001,
    "is_online": 1,
    "mac": "4c:65:a8:da:a8:91"
}
```
To add device by ***mac***
```http
http://host:5000/devices?mac=4C:65:A8:XX:XX:XX
```
```json
{
    "avg_battery": 0.0,
    "avg_humidity": 0.0,
    "avg_temperature": 0.0,
    "is_online": 0,
    "mac": "4c:65:a8:da:a8:91"
}
```
To get online devices
```http
http://host:5000/devices/online
```
```json
[
    {
        "mac": "4c:65:a8:da:a8:91",
        "avg_battery": 99.0,
        "avg_temperature": 27.791000000000025,
        "avg_humidity": 42.06300000000002,
        "is_online": 1
    }
]
```