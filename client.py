import socket
import threading

host = 'localhost'
port = 9999

class tcpclient():
        def __init__(self):
                pass

        def connect(self):
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((host, port))

                server_receiver = threading.Thread(target=self.receive_chat, args=(client_socket,))
                server_receiver.start()

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

"""
def receive_messages(client_socket):
        while True:
                try:
                        # 서버로부터 메시지 수신
                        message = client_socket.recv(1024).decode('utf-8')
                        if not message:
                                print("서버가 연결을 종료했습니다.")
                                break
                        print(f"[server]: {message}")
                except ConnectionResetError:
                        print("서버 연결이 강제로 종료되었습니다.")
                        break

def main():
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        receiver_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receiver_thread.start()

        while True:
                # 서버에게 메시지 전송
                message = input("클라이언트에서 보낼 메시지: ")
                if message == 'quit':
                        break
                client_socket.send(message.encode('utf-8'))

        client_socket.close()

if __name__ == "__main__":
    main()
"""