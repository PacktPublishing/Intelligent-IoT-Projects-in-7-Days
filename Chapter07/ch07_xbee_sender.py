import time
from xbee import DigiMesh
import serial

#PORT = 'COM7'
PORT = '/dev/cu.usbserial-A9CNVHXX'
BAUD_RATE = 9600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = DigiMesh(ser, escaped=True)
import pprint
pprint.pprint(xbee.api_commands)

# xbee with long address
XBEE2_ADDR_LONG = "\x00\x00\x00\x00\x00\x00\xFF\xFF"

while True:
    try:
        print "send data"
        xbee.tx(frame='0x1', dest_addr=XBEE2_ADDR_LONG, data='Hello XBee 2')
        time.sleep(1)
    except KeyboardInterrupt:
        break

xbee.halt()
ser.close()