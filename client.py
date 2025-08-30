import socket

# Client setup
host = '127.0.0.1'   # Server address
port = 5050          # Same port as server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print("Connected to server. Type 'exit' to quit.")

while True:
    msg = input("Client: ")
    client_socket.send(msg.encode())
    if msg.lower() == "exit":
        break
    reply = client_socket.recv(1024).decode()
    print("Server:", reply)

client_socket.close()
