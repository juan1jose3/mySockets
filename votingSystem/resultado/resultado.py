import socket
import json
RESULTADO_IP = socket.gethostbyname(socket.gethostname()) 
print(RESULTADO_IP)
RESULTADO_PORT = 5001
FORMAT = "utf-8"


def handle_client(conn,add):
    
    data = conn.recv(2048).decode(FORMAT)
    if data:
        points = json.loads(data)
        print(f"YES: {points['YES']} ; NO: {points['NO']}")
        
    
    conn.close()




def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as resultado:
        resultado.bind((RESULTADO_IP,RESULTADO_PORT))
        resultado.listen()

        while True:
            conn, add = resultado.accept()
            handle_client(conn,add)
            conn.close()

if __name__ == "__main__":
    main()