import socket
FORMAT = "UTF-8"
UPPER_IP = socket.gethostbyname(socket.gethostname())
PORT = 9090
REVERSER_IP = "172.17.0.4"
REVERSER_PORT = 5001
print(UPPER_IP)


def handle_client(conn,add):
    preguntador_ans = conn.recv(2048).decode(FORMAT)
    if not preguntador_ans:
        return
    
    uppercasing = preguntador_ans.upper()
    
    reverser_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    reverser_sock.connect((REVERSER_IP,REVERSER_PORT))
    
    reverser_sock.send(uppercasing.encode(FORMAT))

    reversedStr = reverser_sock.recv(2048).decode(FORMAT)
    conn.send(reversedStr.encode(FORMAT))
    conn.send(uppercasing.encode(FORMAT))
    conn.close() 

  


    print(f"UPPERCASE: {uppercasing.upper()}")



def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as uppercaser:
        uppercaser.bind((UPPER_IP,PORT))
        uppercaser.listen(5)
        print("Uppercaser listening")

        while True:
            conn,add = uppercaser.accept()
            handle_client(conn,add)
            conn.close()


if __name__ == "__main__":
    main()

