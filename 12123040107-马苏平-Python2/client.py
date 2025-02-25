import socket
host = '192.168.1.101'
port = 9999
addr = (host,port)
buffsize = 1024
with socket.socket(family = socket.AF_INET,type = socket.SOCK_STREAM) as s:
    s.connect(addr)
    print('链接成功')
    msg = input('请输入要发送的信息')
    s.send(msg.encode())
    print('发送成功')
    msg=s.recv(buffsize)
    print('收到数据',msg.encode())
    conn.close()