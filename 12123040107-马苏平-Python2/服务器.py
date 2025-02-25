import socket

host = '10.22.28.101'
port = 9999
serv = (host, port)
buffsize = 1024

with socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) as s:
   s.bind(serv)
   while (True):
      print('正在等待接收数据')
      msg, addr = s.recvfrom(buffsize)
      msg = msg.decode()
      print('从{}收到数据:{}'.format(addr, msg))
      msg =  '你好，发送的信息已收到'
      s.sendto(msg.encode(), addr)
