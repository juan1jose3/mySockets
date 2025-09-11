
import socket
import json
IP = socket.gethostbyname(socket.gethostname())
RESULTADO_IP = "172.17.0.4"
RESULTADO_PORT = 5001
print(IP)

PORT = 9000
FORMAT = "utf-8"

votes = {"YES": 0 , "NO" : 0}

def handle_client(conn,add):
    vote = conn.recv(2048).decode(FORMAT)
    if vote == "YES":
        votes["YES"] +=1
    else:
        votes["NO"] += 1


    resultado_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    resultado_sock.connect((RESULTADO_IP,RESULTADO_PORT))
    resultado_sock.send(json.dumps(votes).encode(FORMAT))
    resultado_sock.close()
    

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as recolector:
        recolector.bind((IP,PORT))
        recolector.listen()
        print("Recolector listening")
        while True: 
            conn, add = recolector.accept()
            handle_client(conn,add)
            conn.close()

if __name__ == "__main__":
    main()