import socket
import threading
import random

    
def handleClient(client_socket, addr):
    print(addr[0])
    keep_communicating = True
    
    while keep_communicating:
        data = client_socket.recv(1024).decode()

        operation, num1, num2 = data.split()
        num1 = int(num1)
        num2 = int(num2)

        if operation == "Close":
            keep_communicating = False
            result = "Closing server"
        elif operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Random":
            result = random.randint(num1, num2)
        client_socket.send(str(result).encode())
    client_socket.close()

host = "192.168.1.127"
port = 12005
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))
serverSocket.listen(1)
print("Server is listning")

while True:
    client_socket = serverSocket.accept()
    threading.Thread(target=handleClient, args= (client_socket)).start()