#!/usr/bin/env python3
"""
A simple HTTP server built using Python's http.server module.

Features:
- Serves a greeting message at the root endpoint (/)
- Serves JSON data at /data
- Returns API status at /status
- Returns API info at /info
- Handles undefined endpoints with a 404 Not Found response
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom request handler for a simple RESTful API."""

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # /data endpoint — return JSON data
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))

        # /status endpoint — return OK
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # /info endpoint — return API info in JSON
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            json_info = json.dumps(info)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_info.encode("utf-8"))

        # Undefined endpoint — return 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(message).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Run the HTTP server on the specified port."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"✅ Server running on port {port}... (http://localhost:{port})")
    print("Press Ctrl+C to stop.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()


if __name__ == "__main__":
    run()
