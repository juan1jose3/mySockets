import socket
import random

class ClienteModelo:
    def __init__(self, host="192.168.2.5", port=5000):  # IP del Cliente 2
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lista =[]

    def conectar(self):
        self.socket.connect((self.host, self.port))

    def generar_numeros(self):
        for _ in range(50):
              self.lista.append(random.randint(0,100))# lista de 50 números diferentes
        return self.lista

    def enviar(self, data):
        mensaje = ",".join(map(str, data))  # convertir lista a string
        self.socket.sendall(mensaje.encode("utf-8"))

    def recibir(self):
        data = self.socket.recv(1024).decode("utf-8")
        return data
