import socket
import threading

HOSTIP = socket.gethostbyname(socket.gethostname())
PORT = 9090
DISCONNECT_MESSAGE = "DISCONNECTED"
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server.bind((HOSTIP,PORT))

clients = []

def handle_host(comm,addr):
    print(f"New Connection {addr}")
    connected = True
    clients.append(comm)
    while connected:
        message = comm.recv(1024).decode("utf-8") # recive
        if message:
              
            print(f"Message from client: {message}")
        
        
        for c in clients:
                if c != comm:
                    c.send(message.encode("utf-8"))

        if message == DISCONNECT_MESSAGE:
            connected = False
            clients.remove(comm)
            print(f"{addr} {message}")      
            comm.close()


        


def get_server_running():
    server.listen()
    print(f"Server listening on: {PORT}")
    
    while True:
        try:
            comm,addr = server.accept()
            thread = threading.Thread(target=handle_host,args=(comm, addr))
            thread.start()
            print(f"Connections: {threading.active_count() - 1}")
        except OSError:
            break


print("Server is starting ....")
print("Server running :) ")

get_server_running() 






