from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #hostname = socket.gethostname()
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        #self.wfile.write("CI/CD con Ansible y Python {hostname}".encode('utf-8'))
        self.wfile.write("CI/CD con Ansible y Python".encode('utf-8'))

server = HTTPServer(("0.0.0.0", 8000), SimpleHandler)
server.serve_forever()
