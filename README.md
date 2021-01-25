# micropython-MH-Z14A
Very simple Micropython library for the MH-Z14A NDIR CO2 sensor. 
Tested to work with ESP32 (specifically a Wemos D32) ~~and probably works with ESP8266~~
Adapted from https://github.com/keepworking/MH-Z14A-PI

# Connections:
UART pin connections can be configured, but these are default:

|  MH-Z14A Pin    |  ESP32   |
| --------------- |:--------:|
|  UART RXD 18    | Pin 18   |
|  UART TXD 19    | Pin 19   |
|     Vin 1       |   5V     |
|     GND 3       |   GND    |

# Example code
```python
import mhz14a
from time import sleep_ms

CO2Sensor = mhz14a.MHZ14A(uartNum=1, rxPin=18, txPin=19)

# CO2 sensor needs to warm up, so after powering up
# initial read may fail as it's still warming up

attempts = 0
ppm=0
while attempts < 3:
    ppm = CO2Sensor.readCO2()
    if ppm > 0:
        print("CO2 value is: " + str(ppm) + " ppm")
        break
    else:
        sleep_ms(500)
     
