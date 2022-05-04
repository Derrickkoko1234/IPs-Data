import time
import socket

print('Starting program...')
time.sleep(5)
print('Generating IPs...')
list_of_ips = []
for i in range(0, 1):
    first = str(1)
    for j in range(0, 6):
        second = str(j)
        print('Done')
        for k in range(0, 256):
            third = str(k)
            for l in range(0, 256):
                forth = str(l)
                ip = first + '.' + second + '.' + third + '.' + forth
                file = open('ips.txt', 'a')
                file.write(ip + '\n')
                # list_of_ips.append(ip)

print('Done')





# ip = socket.gethostbyname('google.com')
