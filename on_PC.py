import serial.tools.list_ports

# connect to the BBB serial port on Windows
x = serial.Serial('COM9', xonxoff=True)

x.write(b'yes "1234567"\n')

while True:
    received = x.readline()
    if received != b'1234567\r\n':
        print(received)

# this prints:
"""
b'yes "1234567"\r\n'
b'11234567\r\n'
b'11234567\r\n'
b'12234567\r\n'
b'12334567\r\n'
b'12345677\r\n'
b'\n'
b'\n'
b'\n'
b'\n'
b'\n'
b'\n'
b'12345567\r\n'
b'\n'
b'12234567\r\n'
b'\n'
b'12334567\r\n'
b'12344567\r\n'
b'12344567\r\n'
b'\n'
b'\n'
b'12344567\r\n'
b'12234567\r\n'
b'12345567\r\n'
b'12345667\r\n'
b'\n'
b'\n'
b'12234567\r\n'
b'12334567\r\n'
b'12234567\r\n'
b'12345677\r\n'
b'12334567\r\n'
b'\n'
b'12345677\r\n'
b'1234567\r\r\n'
b'\n'
b'11234567\r\n'
b'12234567\r\n'
b'123234567\r\n'
b'12234567\r\n'
b'12334567\r\n'
b'\n'
b'12345677\r\n'
b'1234567\r\r\n'
b'12344567\r\n'
b'\n'
b'11234567\r\n'
b'\n'
b'12334567\r\n'
b'12345667\r\n'
b'12234567\r\n'
"""
