import socket
import threading
import os

class tcpserver():
        def __init__(self):
                pass

        def open(self):
                host = os.getenv('host')
                port = int(os.getenv('port'))
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp 연결소켓 생성
                server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #소켓 옵션을 설정하여 이미 사용된 주소를 재사용할 수 있게 합니다.
                server_socket.bind((host, port))
                server_socket.listen()
                print(f"[*] ip : {host} port : {port}")
                while True:
                        client_socket, addr = server_socket.accept()
                        print(f"[+] {addr} connected.")        
                        client_receive = threading.Thread(target=self.receive_chat, args=(client_socket,))
                        client_receive.start()
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

"""
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("클라이언트가 연결을 종료했습니다.")
                break
            print(f"[client]: {message}")
            
            # 클라이언트에게 메시지 전송
            response = input("서버에서 보낼 메시지: ")
            client_socket.send(response.encode('utf-8'))
        except ConnectionResetError:
            print("클라이언트 연결이 강제로 종료되었습니다.")
            break

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = os.getenv('host')
    port = int(os.getenv('port'))
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"[*] ip : {host} port : {port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[+] {addr} connected.")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))-
        client_handler.start()

if __name__ == "__main__":
    main()
"""