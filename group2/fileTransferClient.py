import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server host and port
host = "192.168.0.109"
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Specify the file to send
file_name = "sample.txt"  # Change this to the file you want to send

# Send the file name to the server
client_socket.send(file_name.encode('utf-8'))

# Open and send the file to the server
with open(file_name, 'rb') as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client_socket.send(data)

print(f"Sent file: {file_name}")

# Close the client socket
client_socket.close()
