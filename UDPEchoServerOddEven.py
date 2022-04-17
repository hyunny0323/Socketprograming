#!/usr/bin/python3

import socket

host = ''           # 서버 아이피, '' => 0이 들어감, 커널이 아이피 할당 / 0.0.0.0 = '' 동일
port = 10307
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket 모듈의 socket 함수, 기본적으로 UDP

server_address = (host, port)   # 서버 주소 튜플 생성, 변경 불가
sock.bind(server_address)       # 주소 초기화

while True:
    print("\nwaiting for requests...")

    message, client_address = sock.recvfrom(BUFF_SIZE)     # 값이 없는 경우 recvfrom 에서 Blocking
    print("echo request from {} port {}".format(client_address[0], client_address[1]))  # IP와 Port number 출력
    print("echo message : {}".format(message.decode()))     # 파이썬은 유니코드, 전송할 때는 바이트, 다시 받을 때 decode로 받기 (Byte -> Uni)

    send_message =" "

    if message.decode().isdecimal():

        if int(message.decode()) % 2 == 0:
            print("짝수")
            send_message = "Even number"
        else:
            print("홀수")
            send_message = "Odd number."
    else:
        send_message = "Not number."
        print("숫자X")

    sock.sendto(send_message.encode(), client_address)

sock.close()
