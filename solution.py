import paramiko
import time

# setup logging
paramiko.util.log_to_file('BBB_paramiko.log')
port = 22
hostname = '192.168.7.2'
username = 'root'
password = ''

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password)
stdin, stdout, stderr = client.exec_command('yes 1234567890', bufsize=2**24)
print('streaming started')
startTime = time.perf_counter()
total_data = 0
for i in range(1_000_000):
    line = stdout.readline()
    if line == '1234567890\n':
        total_data += len(line)
    else:
        print(line)
print(f'bytes per second: {int(total_data/(time.perf_counter()-startTime))}')
client.close()
