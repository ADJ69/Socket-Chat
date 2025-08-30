import socket

# Server setup
host = '127.0.0.1'   # Localhost
port = 5050          # Port number

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server started on {host}:{port}, waiting for client...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == "exit":
        print("Connection closed.")
        break
    print("Client:", data)
    reply = input("Server: ")
    conn.send(reply.encode())

conn.close()
