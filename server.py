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
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

client.close()

cap.release()

cv2.destroyAllwindows()


server.close()

