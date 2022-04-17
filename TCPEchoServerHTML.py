#!/usr/bin/python3

import socket

host = '203.250.133.88'     # 서버 아이피
port = 10912                # 서버 포트
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
        html_message = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<HTML><BODY><H1> Hello, World! </H1></BODY></HTML>"
        data_sock.sendall(html_message)

    data_sock.close()
