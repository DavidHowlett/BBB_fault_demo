import paramiko

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
print('streaming started')
stdin, stdout, stderr = client.exec_command(
    'yes 1234567890', bufsize=2**24)
for i in range(1_000_000):
    x = stdout.readline()
    if x != '1234567890\n':
        print(x)
print('finished')
client.close()
