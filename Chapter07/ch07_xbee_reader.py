import time
from xbee import DigiMesh
import serial

#PORT = 'COM8'
PORT = '/dev/cu.usbserial-A601F21U'
BAUD_RATE = 9600


# source
# http://code.activestate.com/recipes/510399-byte-to-hex-and-hex-to-byte-string-conversion/
def ByteToHex(byteStr):
    return ''.join(["%02X" % ord(x) for x in byteStr]).strip()


def decodeReceivedFrame(data):
    source_addr = ByteToHex(data['source_addr'])
    rf_data = data['data']
    options = ByteToHex(data['options'])
    return [source_addr, rf_data, options]


# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object
xbee = DigiMesh(ser, escaped=True)
import pprint
pprint.pprint(xbee.api_commands)

while True:
    try:
        data = xbee.wait_read_frame()        
        decodedData = decodeReceivedFrame(data)
        print(decodedData)

    except KeyboardInterrupt:
        break

xbee.halt()
ser.close()