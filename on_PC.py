import serial.tools.list_ports

# print the names of all the ports on the system
for port in serial.tools.list_ports.comports():
    print(port.device)
# connect to the BBB serial port on OSX
x = serial.Serial('/dev/cu.usbmodem1425')
# repeat the string "HelloWorld" endlessly to stdout
x.write(b'yes HelloWorld\n')
while True:
    received = x.readline()
    if received != b'HelloWorld\r\n':
        print(received)

# This program prints the below lines, I get 1 error every ~700 milliseconds on OSX.
"""
/dev/cu.Bluetooth-Incoming-Port
/dev/cu.usbmodem1425
b'\n'
b'HelloWorld\r\r\n'
b'HelloW\r\n'
b'HelloWorHelloWorld\r\n'
b'HelHelloWorld\r\n'
b'HelHelloWorld\r\n'
b'\r\n'
b'HeHelloWorld\r\n'
b'HelloWHelloWorld\r\n'
b'HelloWorlHelloWorld\r\n'
b'HeHelloWorld\r\n'
b'HelloWorldHelloWorld\r\n'
b'HelloWHelloWorld\r\n'
b'HelloWorHelloWorld\r\n'
b'HelloWorldHelloWorld\r\n'
b'HelloWHelloWorld\r\n'
b'HelloHelloWorld\r\n'
b'HelHelloWorld\r\n'
b'HelHelloWorld\r\n'
b'HHelloWorld\r\n'
b'HelloWorldHelloWorld\r\n'
"""
