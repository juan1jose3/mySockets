class ClienteVista:
    def mostrar_numeros(self, numeros, quien="Cliente 1"):
        if quien == "Cliente 1":
            print(f"Recibido del {quien}:")
        else:
            print(f"Enviar cliente 1")
            
        print(numeros)

    def preguntar_respuesta(self):
        opcion = input("¿Quieres enviar tu lista al Cliente 1? (s/n): ")
        return opcion.lower() == "s"
