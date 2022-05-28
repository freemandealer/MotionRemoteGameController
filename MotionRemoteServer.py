import socket
import mmap
import os
from time import *
f = os.open("C:\\Users\\Administrator\\Desktop\\mapfile",os.O_RDWR)
# mm = mmap.mmap(f, 0)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('192.168.43.56',8080))
print("binding complete")
server.listen(5)
print("listen complete")
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
                    with mmap.mmap(f, 0) as mm:
                        mm[1] = ord('L')
                        #mm.flush()
                elif (v < -4):
                    with mmap.mmap(f, 0) as mm:
                        mm[1] = ord('l')
                        #mm.flush()
                elif (v > 11):
                    with mmap.mmap(f, 0) as mm:
                        mm[1] = ord('R')
                        #mm.flush()
                elif (v > 5):
                    with mmap.mmap(f, 0) as mm:
                        mm[1] = ord('r')
                        #mm.flush()
                else:
                    with mmap.mmap(f, 0) as mm:
                        mm[1] = ord('m')
                        #mm.flush()
            elif s == '0':
                if abs(v - 9.9) > 0.2:
                    stop = 0
                    with mmap.mmap(f, 0) as mm:
                        mm[0] = ord('w')
                        #mm.flush()
                else:
                    with mmap.mmap(f, 0) as mm:
                        if (stop < 4):
                            stop = stop + 1
                        else:
                            mm[0] = ord('s')
                            #mm.flush()
                
    conn.close()
mm.close()	
os.close(f)