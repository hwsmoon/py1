#!/usr/bin/python3

import socket
host = ''
port = 10202
BUFF_SIZE=128

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = (host,port)
sock.bind(server_address)

while True:
    print("n\waiting for request...")
    message, client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request from {} port {}".format(client_address[0],client_address[1]))
    print("echo message : {}".format(message.decode()))
    data=message.decode()
    try:
        num = int(data)
        if num % 2:
            answer = "홀수"
        else:
            answer = "짝수"
    except valueError:
        answer = "숫자가 아님"
    sock.sendto(answer.encode(), client_address)

sock.close
