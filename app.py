from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = {
            "message": "Python CI/CD pipeline is working fine!",
            "path": self.path,
            "status": "healthy"
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(("0.0.0.0", 8000), AppHandler)
print("Python application running on port 8000")
server.serve_forever()
