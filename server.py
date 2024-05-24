import socket
import threading
import os

class tcpserver():
        def __init__(self):
                pass

        def open(self):
                host = os.getenv('host')
                port = int(os.getenv('port'))
                #tcp socket create
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                #Set the socket option to allow reuse of an already used address
                server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
                server_socket.bind((host, port))
                server_socket.listen()
                print(f"[*] ip : {host} port : {port}")
                while True:
                        client_socket, addr = server_socket.accept()
                        print(f"[+] {addr} connected.")
                        #set to receive message from client to thread
                        client_receive = threading.Thread(target=self.receive_chat, args=(client_socket,))
                        client_receive.start()
                        #set to send message from client to thread
                        client_sender = threading.Thread(target=self.send_chat, args=(client_socket,))
                        client_sender.start()

        def receive_chat(self,client_socket):
                while True:
                        try:
                                message = client_socket.recv(1024).decode('utf-8')
                                print(f"[R]: {message}")
                        except ConnectionResetError:
                                print("\nclient disconnected")
                                break
                client_socket.close()

        def send_chat(self,client_socket):
                while True:
                        try:
                                response = input('')
                                client_socket.send(response.encode('utf-8'))
                        except:
                                client_socket.send("Error 404".encode('utf-8'))
                                break
                client_socket.close()

chatting_server = tcpserver()
chatting_server.open()
