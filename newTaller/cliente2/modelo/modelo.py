import socket
import random

class ClienteModelo:
    def __init__(self, host="192.168.2.5", port=5000):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None  # conexión con Cliente 1
        self.lista = []

    def escuchar(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Cliente 2 escuchando en {self.host}:{self.port}...")
        self.conn, addr = self.socket.accept()
        print(f"Cliente 2 conectado por {addr}")

    def recibir(self):
        data = self.conn.recv(1024).decode("utf-8")
        numeros = list(map(int, data.split(",")))  # convertir string a lista de enteros
        return numeros

    def generar_numeros(self):
        for _ in range(50):
              self.lista.append(random.randint(0,100))# lista de 50 números diferentes
        return self.lista

    def enviar(self, data):
        mensaje = ",".join(map(str, data))  # convertir lista a string separado por comas
        self.conn.sendall(mensaje.encode("utf-8"))

    def cerrar(self):
        if self.conn:
            self.conn.close()
        self.socket.close()
