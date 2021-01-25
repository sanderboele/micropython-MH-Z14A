from machine import UART
from time import sleep_ms, ticks_ms, ticks_diff, sleep_us

class MHZ14A():
    packet = [0xFF,0x01,0x86,0x00,0x00,0x00,0x00,0x00,0x79]

    def __init__(self, uartNum=1, txPin=18, rxPin=19):
        """initializes communication with CO2 sensor"""
        self.uart = UART(uartNum, 9600)
        self.uart.init(parity=None, stop=1, bits=8, rx=rxPin, tx=txPin)
        # wait a minimum amount of time before trying to read the sensor
        sleep_ms(250)

    def readCO2(self):
        """reads CO2 concentration from MH-Z14a sensors and returns ppm value"""
        packet = [0xFF,0x01,0x86,0x00,0x00,0x00,0x00,0x00,0x79]
        try:
            # flush serial
            while self.uart.any() > 0:
                self.uart.read(self.uart.any())
            self.uart.write(bytearray(packet))
            start = ticks_ms()
            while self.uart.any() < 9:
                if ticks_diff(ticks_ms(), start) > 5000:
                    print("Timeout reading CO2 sensor")
                    return -4
            res = self.uart.read(9)
            if res is not None and len(res)==9:
                checksum = 0xff & (~(res[1]+res[2]+res[3]+res[4]+res[5]+res[6]+res[7])+1)
                if res[8] == checksum:
                    res = bytearray(res)
                    ppm = (res[2]<<8)|res[3]
                    return ppm
                else:
                    print("CO2 sensor reading checksum failed. Result was: ", res)
                    return -1
            else:
                print("CO2 sensor did not return data")
                return -2
        except Exception as e:
            print("Exception reading sensor:")
            print(str(e))
            return -3
