#!/usr/bin/python3
# 쇼뱅? 파이썬 스크립트 처리

import socket

# host = '203.250.133.88'     # 서버 아이피
host = ''     # 서버 아이피
port = 14912                # 서버 포트
BUFF_SIZE = 128
BACKLOG = 5

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# socket 모듈의 socket 함수, 기본적으로 UDP

server_address = (host, port)   # 서버 주소 튜플 생성, 변경 불가
conn_sock.bind(server_address)

conn_sock.listen(BACKLOG)

while True:
    print("Waiting for requests...")
    data_sock, address = conn_sock.accept()
    print("echo request from {} port {}".format(address[0], address[1]))
    message = data_sock.recv(BUFF_SIZE)

    if message:
        print("recevied message : {}\n".format(message.decode()))

        try:
            fd = open(message.decode(), 'r', encoding='UTF-8')

            for line in fd:
                data_sock.sendall(line.encode())

        except FileNotFoundError as e:
            print(e)
            print("존재하지 않는 파일 이름 입니다.")
            data_sock.sendall("0".encode())

    data_sock.close()
    fd.close()

