#!/usr/bin/python3
# 쇼뱅? 파이썬 스크립트 처리

import socket

host = '203.250.133.88'     # 서버 아이피
port = 14912                # 서버 포트
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# socket 모듈의 socket 함수, 기본적으로 UDP

server_address = (host, port)   # 서버 주소 튜플 생성, 변경 불가
print("connecting to {} port {}".format(server_address[0], server_address[1]))
sock.connect(server_address)

message = input("Enter File name : ")
message = bytes(message, encoding='utf-8')

try:
    sock.sendall(message)

    while True:
        data = sock.recv(BUFF_SIZE)
        fd = open(message.decode(), 'a')
        if data:
            fd.write(data.decode())
        else:
            break

except Exception as e:
    print("Exception {}".format(e))

sock.close()
