class ClienteVista:
    def preguntar_envio(self):
        opcion = input("¿Quieres enviar 50 números al cliente 2? (s/n): ")
        return opcion.lower() == "s"

    def mostrar_respuesta(self, mensaje):
        print(f"Cliente 2 respondió: {mensaje}")
