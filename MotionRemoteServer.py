import socket
import os
from time import *
import vXboxInterfacePythonWrapper.vXboxInterface as ctrlr

server = []

def init_ctrlr():
    res = ctrlr.isVBusExists()
    if res:
        print("Virtual Xbox bus exists")
    else:
        print("Virtual Xbox bus dose not exist, please download and install")
        print("https://github.com/nefarius/ScpToolkit/files/239098/ScpVBus_x64.zip")

    res = ctrlr.isControllerExists(1)
    if res:
        print("controller already exists, quit")
        exit(-1)
    res = ctrlr.isControllerOwned(1)
    if res:
        print("controller is owned by another program, quit")
        exit(-1)
    res = ctrlr.PlugIn(1)
    if res:
        print("controller plugged in successfully")
    else:
        print("controller plugged in failed")
        exit(-1)

def init_network():
    global server
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('0.0.0.0',8080))
    print("binding complete")
    server.listen(5)
    print("listen complete")

init_ctrlr()

init_network()

stop = 3
while True:
    print("listening")
    conn,addr = server.accept()
    print("accepted")
    print(conn,addr)

    while True:
        data = conn.recv(16)
        if data and len(data.decode().split(' ')) >= 3:
            d = data.decode().split(' ')[0]
            s = data.decode().split(' ')[1]
            v = float(data.decode().split(' ')[2])
            if s == '1':
                if (v < -11):
                    ctrlr.SetAxisRx(1,-20000)
                elif (v > 11):
                    ctrlr.SetAxisRx(1,20000)
                else:
                    a = int(v*v*165)
                    if v < 0:
                        a = -a
                    ctrlr.SetAxisRx(1,a)
            elif s == '0':
                if abs(v - 9.9) > 0.2:
                    stop = 0
                    ctrlr.SetAxisY(1,32000)
                else:
                    if (stop < 4):
                        stop = stop + 1
                    else:
                        ctrlr.SetAxisY(1,0)

    conn.close()
