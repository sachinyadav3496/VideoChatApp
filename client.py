import socket
import os
import cv2

client = socket.socket()

client.connect(('localhost', 12345))

print("connected")



while True:
    s = client.recv(20)
    print(s)
    size = int(s.decode())
    print("size: ", size)
    recv_size = 0
    fp = open('test_recv.jpg', 'wb')
    while recv_size < size:
        data = client.recv(size)
        fp.write(data)
        recv_size += len(data)
    print("Received: ", recv_size)
    fp.close()

    print("Size Received: ", os.path.getsize('test_recv.jpg'))
    im = cv2.imread('test_recv.jpg')
    cv2.imshow('Image', im)
    cv2.waitKey(1)

print("sucessfull")

client.close()
