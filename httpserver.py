#modified starting from https://gist.github.com/joaoventura/824cbb501b8585f7c61bd54fec42f08f
import socket
import scene

myScene=scene.Scene()

def handle_request(request):
    print(request)

    try:
        #content=web.textSlashdot
        myScene.switchScene()
        
        response = 'HTTP/1.0 200 OK\n\n'
        #response = 'HTTP/1.0 200 OK\n\n' + content
        #response = 'HTTP/1.1 200 OK\nContent-Type: text/plain\nAccess-Control-Allow-Origin: *\n\n' + content
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    return response


# Define socket host and port
SERVER_HOST = '0.0.0.0'
#SERVER_PORT = 8080
#SERVER_PORT = 9000
SERVER_PORT = 5000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Return an HTTP response
    response = handle_request(request)
    client_connection.sendall(response.encode())

    # Close connection
    client_connection.close()

# Close socket
server_socket.close()
