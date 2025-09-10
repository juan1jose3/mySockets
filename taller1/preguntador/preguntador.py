import socket
import threading
SERVER_IP = "172.17.0.4"
PORT = 9003
DISCONNECT_MESSAGE = "DISCONNECTED"

client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client1.connect((SERVER_IP,PORT))







def send_message():
    while True:
        msg = input("a,b,c: ")


        client1.send(msg.encode("utf-8"))
        if msg == DISCONNECT_MESSAGE:
            break

    

thread2 = threading.Thread(target=send_message)
thread2.start()
