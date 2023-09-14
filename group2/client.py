import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server host and port
host = "10.60.29.41"  # localhost
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Send data to the server
message = "Hello, Server!"
client_socket.send(message.encode('utf-8'))

# Receive and print the response from the server
response = client_socket.recv(1024).decode('utf-8')
print(f"Server response: {response}")

# Close the client socket
client_socket.close()
