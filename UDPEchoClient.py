#!/usr/bin/python3

import socket

host = '203.250.133.88'     # 서버 아이피
port = 10307                # 서버 포트
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (host, port)
#my_address('localhos', 20123)
#sokect.bind(my_address) 를 하지 않는 이유, 충돌 가능성 배제, 커널에게 맡김

message = input("Enter message : ")
message = bytes(message, encoding='utf-8')
#message = message.encode('utf-8')
#message = message.encode()

try:
    byte_send = sock.sendto(message, server_address)
    data, address = sock.recvfrom(BUFF_SIZE)
    print("Received from server : {}".format(data.decode()))    # Byte -> UNI code
except Exception as e:
    print("Exception : {}".format(e))

sock.close()
