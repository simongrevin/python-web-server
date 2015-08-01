def handle_request(path):
	if path == '/welcome':
		return 'Bienvenue simon'
	elif path == '/about':
		return '<h1>ABOUT</h1>'
	else:
		return 'gtfo'
