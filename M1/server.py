import http.server
import socketserver
from sys import argv

PORT = 7777

Handler = http.server.SimpleHTTPRequestHandler

if __name__ == "__main__":

    if len(argv) > 1:
        PORT = int(argv[1])

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()
