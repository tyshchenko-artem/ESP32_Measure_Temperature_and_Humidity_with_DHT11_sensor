<h1>Programming ESP32 board with MicroPython project</h1>
 <hr>
<h2>Initial Setup of ESP32 board</h2>
First of all, install MicroPython on ESP32.

<code>boot.py</code> file is used for config REPL Wi Fi connection with ESP32 board on boot. Please provide <code>secrets.py</code>
file with these settings of your Wi Fi:

<code>wifi_name</code> - name of your Wi Fi network;

<code>wifi_password</code> - password of your Wi Fi network;

<hr>
<code>dht11_sensor.py</code> file contains code that can be used for measure temperature and humidity of current 
environment using DHT11 sensor connected to ESP32 board.