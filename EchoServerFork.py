#!/usr/bin/python3
import os
import sys
import errno
import signal
import socket

BACKLOG = 5
host = "0.0.0.0"
port = 10002

def collect_zombie(signum,frame):
    while True:
        try:
            pid,status = os.waitpid(-1,os.WNOHANG)
            if pid == 0:
                break
        except:
            break

def do_echo(sock):
    while True:
        message = sock.recv(1024)
        if message:
            sock.sendall(message)
        else:
            return

signal.signal(signal.SIGCHLD,collect_zombie)

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
conn_sock.bind((host,port))
conn_sock.listen((BACKLOG))

print('Listening on port %d...'%port)

while True:
    try:
        data_sock, client_address = conn_sock.accept()
    except IOError as e:
        code, msg = e.args
        if code == errno.EINTR:
            continue
        else:
            raise

    pid = os.fork()
    if pid ==0:
        conn_sock.close()
        do_echo(data_sock)
        os._exit(0)

    data_sock.close()