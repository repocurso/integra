from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"¡Hola, CI/CD con Ansible y Python!")

server = HTTPServer(("0.0.0.0", 8000), SimpleHandler)
server.serve_forever()
