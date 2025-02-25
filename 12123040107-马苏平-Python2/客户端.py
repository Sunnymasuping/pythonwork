import socket

host = '10.203.167.23'
port = 9999
addr = (host, port)
buffsize = 1024

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
   msg = input('请输入要发送的信息：')
   s.sendto(msg.encode(), addr)
   print('发送成功')
   msg = s.recv(buffsize)
   print('收到数据', msg.decode())
   s.close()