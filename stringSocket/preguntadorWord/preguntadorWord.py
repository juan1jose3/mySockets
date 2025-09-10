import socket
SERVER_IP = "172.17.0.3"
PORT = 9090
FORMAT = "utf-8"
preguntador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
preguntador.connect((SERVER_IP,PORT))


word = input("Type something: ")
preguntador.send(word .encode(FORMAT))
reversedStr = preguntador.recv(2048).decode(FORMAT)
print(reversedStr)
answer = preguntador.recv(2048).decode(FORMAT)
print(answer)
preguntador.close()