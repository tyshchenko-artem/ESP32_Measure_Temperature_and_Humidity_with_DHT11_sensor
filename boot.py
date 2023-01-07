# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
from secrets import wifi_name, wifi_password

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wifi_name, wifi_password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()
webrepl.start()
