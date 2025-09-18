from modelo.modelo import ClienteModelo
from vista.vista import ClienteVista

class ClienteControlador:
    def __init__(self):
        self.modelo = ClienteModelo()
        self.vista = ClienteVista()

    def ejecutar(self):
        self.modelo.conectar()
        if self.vista.preguntar_envio():
            numeros = self.modelo.generar_numeros()
            self.modelo.enviar(numeros)
            respuesta = self.modelo.recibir()
            self.vista.mostrar_respuesta(respuesta)
        else:
            print("No se enviaron los números.")
