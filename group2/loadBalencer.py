import socket
import threading
from queue import Queue
import storeMetaData

# List of storage server IP addresses and ports
storage_servers = [("10.60.11.29", 12345),("10.60.4.110", 12345)]

# Create a queue to manage incoming data streams
data_queue = Queue()
# Adding items to the queue
data_queue.put("sample1.txt".encode('utf-8'))
data_queue.put("sample2.txt".encode('utf-8'))
data_queue.put("sample3.txt".encode('utf-8'))
data_queue.put("sample4.txt".encode('utf-8'))
data_queue.put("sample5.txt".encode('utf-8'))
data_queue.put("sample6.txt".encode('utf-8'))


def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            data_queue.put(data)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

# Function to forward data to storage servers
def forward_data_to_servers():
    current_server = 0
    while True:
        data = data_queue.get()
        storage_server = storage_servers[current_server]
        metadata={"fileName":data.decode("utf-8"),"location":storage_server}

        try:
            # Forward the data to the storage server
            storage_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            storage_socket.connect(storage_server)
            storage_socket.send(data)
            storeMetaData.connectDatabase(metadata)
            storage_socket.close()
        except Exception as e:
            print(f"Error forwarding data to {storage_server}: {e}")

        current_server = (current_server + 1) % len(storage_servers)

# Start the data forwarding thread
data_forwarder_thread = threading.Thread(target=forward_data_to_servers)
data_forwarder_thread.start()

# Create a socket for load balancer to accept incoming connections
load_balancer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
load_balancer.bind(("localhost", 8080))
load_balancer.listen(5)

# while True:
#     client, addr = load_balancer.accept()
#     client_handler = threading.Thread(target=handle_client, args=(client,))
#     client_handler.start()