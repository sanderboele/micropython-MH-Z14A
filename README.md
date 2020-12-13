# micropython-MH-Z14A
Micropython library for the MH-Z14A NDIR CO2 sensor. 
Tested to work with ESP32 and probably works with ESP8266

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
CO2Sensor = mhz14a.MHZ14A(uartNum=1, rxPin=18, txPin=19)

attempts = 0
ppm=0
while attempts < 3:
    ppm = CO2Sensor.readCO2()
    if ppm != -1:
        print("CO2 value is: " + str(ppm) + " ppm")
        break
    else:
        sleep_ms(250)
     
