import socket
import os
import cv2


cap = cv2.VideoCapture(0)

server = socket.socket()
server.bind(('localhost', 12345))
server.listen()

client, addr = server.accept()

print("client: ", addr)

while True:
    _, im = cap.read()
    cv2.imwrite('test.jpg', im)
    
    fp = open("test.jpg", 'rb')

    client.send(f"{os.path.getsize('test.jpg')}".encode())


    client.sendfile(fp)

    fp.close()
    
    cv2.waitKey(100)
    s = client.recv(5)
    print(s)
    size = int(s.decode())
    print("Size: ", size)
    recv_size = 0
    file_data = open('test_recv1.jpg', 'wb')
    print("opend file")
    while recv_size < size:
        data = client.recv(size)
        file_data.write(data)
        recv_size += len(data)
        print('received data: ', recv_size)
    file_data.close()
    print("Recevied file")
    im = cv2.imread('test_recv1.jpg')
    cv2.imshow('Image1', im)
    cv2.waitKey(10)



client.close()

cap.release()

cv2.destroyAllwindows()


server.close()

