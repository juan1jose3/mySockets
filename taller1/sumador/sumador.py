import socket
import threading

HOSTIP = socket.gethostbyname(socket.gethostname())
PORT = 9003
DISCONNECT_MESSAGE = "DISCONNECTED"
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
server.bind((HOSTIP,PORT))

clients = []
userInput = []
results = [] 




def handle_host(comm,addr):
    print(f"New Connection {addr}")
    connected = True
    index = 0
    clients.append(comm)
    
    while connected:
        message = comm.recv(1024).decode("utf-8") 
        if message and "," in message:
              
            print(f"Message from client: {message}")
            userInput.append(int(message[0]))
        elif "," not in message and message:
            results.append(int(message))
            ans = userInput[index] + results[index]
            print(f"a+(b-c) = {ans}")
            index += 1
            
            
           
        
            
        
        
        for client in clients:
                if client != comm:
                    client.send(message.encode("utf-8"))

        
        
                    

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
print(HOSTIP)

get_server_running() 