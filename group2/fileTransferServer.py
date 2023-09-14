import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port for the server
host = "10.60.29.41"
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

    # Receive the file name
    file_name = client_socket.recv(1024).decode('utf-8')

    # Open a new file to write the received data
    with open(file_name, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print(f"Received file: {file_name}")

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()
