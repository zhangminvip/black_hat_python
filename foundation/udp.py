import socket

target_host = '127.0.0.1'
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto('ABCD', (target_host, target_port))
data, addr = client.recvfrom(4096)
print data

# class Flowler:
#
#     def __init__(self):
#         self.__color = 'Red'
#
#
# rose = Flowler()
# print rose._Flowler__color