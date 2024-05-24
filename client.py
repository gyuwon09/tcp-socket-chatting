import socket
import threading

host = 'localhost'
port = 9999

class tcpclient():
        def __init__(self):
                pass

        def connect(self):
                #client socket create
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((host, port))
                #set to receive message from server to threading
                server_receiver = threading.Thread(target=self.receive_chat, args=(client_socket,))
                server_receiver.start()
                #set to send message from server to threading
                server_sender = threading.Thread(target=self.send_chat, args=(client_socket,))
                server_sender.start()

        def receive_chat(self,client_socket):
                while True:
                        try:
                                message = client_socket.recv(1024).decode('utf-8')
                                print(f"[R]: {message} ")
                        except ConnectionResetError:
                                print("server disconnected")
                                break

        def send_chat(self,client_socket):
                while True:
                        try:
                                message = input("")
                                if message == 'quit':
                                        break
                                client_socket.send(message.encode('utf-8'))
                        except:
                                client_socket.send("client Error".encode('utf-8'))
                                break

chatting_client = tcpclient()
chatting_client.connect()
