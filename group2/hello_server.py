import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port for the server
host = "10.60.29.41"  # localhost
port = 12345

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {host}:{port}")

while True:
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break

    print(f"Received data: {data}")

    # Send the received data back to the client
    client_socket.send(data.encode('utf-8'))

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()
