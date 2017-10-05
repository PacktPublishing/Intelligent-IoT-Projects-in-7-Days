from respeaker import gpio

gpio18 = gpio.Gpio(18, gpio.DIR_OUT)
# turn on LED
gpio18.write(1)
# turn off LED
gpio18.write(0)

# close gpio
gpio18.close()
