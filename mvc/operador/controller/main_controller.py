import socket
from model.calculator_model import CalculatorModel
from view.console_view import ConsoleView

class MainController:
    def __init__(self, host='0.0.0.0', port=65432):
        self.model = CalculatorModel()
        self.view = ConsoleView()
        self.host = host
        self.port = port

    def run(self):
        # Start socket server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            self.view.show_message(f"Operator listening on {self.host}:{self.port}...")
            
            while True:
                conn, addr = s.accept()
                with conn:
                    self.view.show_message(f"Connected by {addr}")
                    data = conn.recv(1024)
                    if not data:
                        continue
                    try:
                        a_str, b_str, op = data.decode().split(',')
                        a = int(a_str)
                        b = int(b_str)
                        result = self.model.calculate(a, b, op)
                    except Exception as e:
                        result = f"Error: {e}"
                    conn.sendall(str(result).encode())
