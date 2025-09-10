import socket

RECOLECTOR_IP = "172.17.0.4"
PORT = 9000
FORMAT = "utf-8"

while True:
    vote = input("YES OR NO: ")

    if vote == "EXIT":
        break

    votador = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    votador.connect((RECOLECTOR_IP,PORT))
    votador.send(vote.encode(FORMAT))

votador.close()

