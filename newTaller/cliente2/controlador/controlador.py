from modelo.modelo import ClienteModelo
from vista.vista import ClienteVista

class ClienteControlador:
    def __init__(self):
        self.modelo = ClienteModelo()
        self.vista = ClienteVista()

    def ejecutar(self):
        try:
            self.modelo.escuchar()  # Espera la conexión de Cliente 1
            numeros_recibidos = self.modelo.recibir()
            self.vista.mostrar_numeros(numeros_recibidos, "Cliente 1")

            # Generar lista de 50 números y enviarla de vuelta a Cliente 1
            numeros_a_enviar = self.modelo.generar_numeros()
            self.modelo.enviar(numeros_a_enviar)
            self.vista.mostrar_numeros(numeros_a_enviar, "Cliente 2")

        finally:
            self.modelo.cerrar()

