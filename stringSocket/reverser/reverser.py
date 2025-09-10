import socket
REVERSER_IP = socket.gethostbyname(socket.gethostname())
REVERSER_PORT = 5001
FORMAT = "utf-8"
print(REVERSER_IP)


def handle_client(conn,add):
    uppercaser_ans = conn.recv(2048).decode(FORMAT)
    if not uppercaser_ans:
        return
    reverseStr = uppercaser_ans[::-1]
    print(f"REVERSED: {reverseStr}")
    conn.send(reverseStr.encode(FORMAT))


def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as reverser:
        reverser.bind((REVERSER_IP,REVERSER_PORT))
        reverser.listen()
        while True:
            conn,add = reverser.accept()
            handle_client(conn,add)
            conn.close()

if __name__ == "__main__":
    main()


