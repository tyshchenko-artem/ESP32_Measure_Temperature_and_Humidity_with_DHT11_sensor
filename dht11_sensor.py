from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(4))
led = Pin(2, Pin.OUT)

def call_dht11(sens):
  try:
    sleep(1)
    print("Sensor takes a measure...")
    sens.measure()
    temp = sens.temperature()
    hum = sens.humidity()
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')

while True:
    sleep(1)
    call_dht11(sensor)
    led.value(not led.value())