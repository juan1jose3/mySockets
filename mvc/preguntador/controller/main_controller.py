import socket
from model.data_model import DataModel
from view.console_view import ConsoleView

class MainController:
    def __init__(self):
        self.model = DataModel()
        self.view = ConsoleView()

    def run(self):
        # Get input from user
        a, b, op = self.view.get_input()
        self.model.a = a
        self.model.b = b
        self.model.operation = op

        # Connect to operator container
        operator_host = "operadorMvc"  # Container name in Docker network
        operator_port = 65432

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((operator_host, operator_port))
                message = f"{self.model.a},{self.model.b},{self.model.operation}"
                s.sendall(message.encode())
                data = s.recv(1024)
            self.view.show_result(data.decode())
        except Exception as e:
            print(f"Error connecting to operator: {e}")
