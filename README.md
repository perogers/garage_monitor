# garage_monitor
This is a Raspberry Pi application using Flask that returns an image and ambient temperature of a monitored location.

A cron job executes single_shot.py every minute to take a picture of the garage door.

Additionally cron runs garage_cam.sh to ensure the flask application is running.

A temperature sensor (Dallas DS18B20) is used to obtain the garage temperature.

**If exposed to the Internet this application should be run as a no login user**

Requires:

1. RPi.GPIO

2. [Thermal Sensor Library](https://github.com/timofurrer/w1thermsensor)
