import socket
import app

HOST,  PORT = '', 8888

# addresse family and socket type
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# allow to reuse the same address
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind
listen_socket.bind((HOST, PORT))

# listen
listen_socket.listen(1)

print 'HTTP servi sur le port %s ...' % PORT

name = 'Simon';

while True:

	client_connection, client_address = listen_socket.accept()

	request = client_connection.recv(1024)



	request_line = request.splitlines()[0]
	request_line = request_line.rstrip('\r\n')
	# Break down the request line into components
	(request_method,  # GET
	 path,            # /hello
	 request_version  # HTTP/1.1
	) = request_line.split()
	
	print path

	http_response = """\
	HTTP/1.1 200 OK

	Response : """ + app.handle_request(path) + """
	"""

	client_connection.sendall(http_response)
	client_connection.close()