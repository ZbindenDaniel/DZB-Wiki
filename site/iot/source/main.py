# main.py
"""
This files runs after boot.

# Functionality:
    - Setup interrupts to wake up from deep sleep by button push
    - Check if file file 'notUpdatable' exists, if so put its contents into the queue to send to the cloud
    - if woken up from deep sleep by a timer, run the DataCollector
    - if woken up by the interrupt, run a Wifi Access point for a defined amount of time (from config)
    - Go into deep sleep mode (machine.deepsleep) for 30 minutes
"""

#import ugit
import utime
#import webserver
from ledControl import Led
from logger import logger
from machine import Pin, ADC
import dht

log = logger("main", 1, True)

#backup() # good idea to backup your files!
led = Led()
led.start(22)


adc = ADC(Pin(26, mode=Pin.IN))
d = dht.DHT22(machine.Pin(4))
while True:
    d.measure()
    print(f'adc: {adc.read_u16()} - dht: {d.temperature()}')
    utime.sleep(3)
#webserver.runServerFor() # also have webclient, webclient uses ugit
# if connected
# TODO: Test again --> ugit.pull_all()
