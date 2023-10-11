import socket

serverHost = "192.168.1.127"
serverPort = 12005
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((serverHost, serverPort))

keep_communicating = True

while keep_communicating:
    operation = input("Enter one of the following operation: Add/Subtract/Random: ")
    if operation == "Close":
        keep_communicating = False
    else:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        request = f"{operation} {num1} {num2}"
        client.send(request.encode())
        result = client.recv(1024).decode()
        print("Result: ", result)
client.close()