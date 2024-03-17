import socket

# Function to retrieve hostname for the server IP
def get_hostname():
    try:
        # Get the hostname of the local machine
        hostname = socket.gethostname()
        # Get the IP address corresponding to the hostname
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None

# Create a TCP socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Get the server IP address
host = get_hostname()  # Host is the server IP
port = 4444  # Port to Listen On

# Binding to the socket
serversocket.bind((host, port))

# Starting TCP listener
serversocket.listen(3)

print(f"Server listening on {host}:{port}")

while True:
    # Accept incoming connections
    clientsocket, address = serversocket.accept()
    print(f"Received connection from {address}")

    # Message to send to the client after successful connection
    message = 'All right, you found the way! Thank you for connecting to the server.\n'
    clientsocket.send(message.encode('ascii'))

    # Close the client socket
    clientsocket.close()
