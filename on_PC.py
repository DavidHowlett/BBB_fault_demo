import serial

x = serial.Serial('COM15')
to_send = b'\x03yes HelloWorld\n'
x.write(to_send)
while True:
    received = x.readline()
    if received != b'HelloWorld\r\n':
        print(received)
