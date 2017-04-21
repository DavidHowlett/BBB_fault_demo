import serial

x = serial.Serial('COM15')
to_send = b'debian\ntemppwd\npython3.6 on_BBB.py\n'
x.write(to_send)
while True:
    received = x.readline()
    if len(received) != 26:
        print(received)