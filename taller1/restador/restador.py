import socket
import threading
SERVER_IP = "172.17.0.4"
PORT = 9003
DISCONNECT_MESSAGE = "DISCONNECTED"

client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client1.connect((SERVER_IP,PORT))




def send_message():
    while True:
        numbers = client1.recv(2048).decode("utf-8")
        if numbers:
            a,b,c = numbers.split(",")

            result = int(b) - int(c)
            print(result)
            client1.send(str(result).encode("utf-8"))


    
    

thread = threading.Thread(target=send_message)
thread.start()


