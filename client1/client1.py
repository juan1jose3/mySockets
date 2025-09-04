import socket
import threading
SERVER_IP = "192.168.10.114"
PORT = 9090
DISCONNECT_MESSAGE = "DISCONNECTED"

client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client1.connect((SERVER_IP,PORT))


welcome = client1.send("Hello from client".encode("utf-8"))

def decoding_message():
    while True:
        try:
            msg = client1.recv(2048).decode("utf-8")
            if not msg:
                break
            print(f"Reply:{msg}")
        except:
            break


def send_message():
    while True:
        msg = input("Message client1: ")
        client1.send(msg.encode("utf-8"))
        if msg == DISCONNECT_MESSAGE:
            break

    
    

thread = threading.Thread(target=decoding_message)
thread.start()

thread2 = threading.Thread(target=send_message)
thread2.start()

       
    


