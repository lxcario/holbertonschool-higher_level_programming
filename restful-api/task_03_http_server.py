#!/usr/bin/python3
"""
Module to implement a basic HTTP server using Python's http.server module,
demonstrating endpoint routing and JSON response handling.
"""
import http.server
import json
import sys

# Define the port the server will run on
PORT = 8000

class HTTPHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler that processes GET requests for different endpoints.
    """

    def do_GET(self):
        """Method to handle all incoming GET requests and route them by path."""

        # 1. Root endpoint (/)
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write('Hello, this is a simple API!'.encode('utf-8'))

        # 2. /data endpoint (Serving JSON)
        elif self.path == '/data':
            self.send_response(200)
            # Set the header to indicate a JSON response
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            # Convert Python dict to JSON string and encode to bytes
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # 3. /status endpoint
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        # 4. /info endpoint (Required for the expected output)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # 5. 404 Error handler (for all undefined paths)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            # FIX: Ensure content is exactly 'Not Found' to pass the test
            self.wfile.write('Not Found'.encode('utf-8'))


if __name__ == '__main__':
    """Server initialization and run loop."""
    try:
        server_address = ('', PORT)
        httpd = http.server.HTTPServer(server_address, HTTPHandler)
        print(f"Starting server on port {PORT}...")
        
        # This function runs the server indefinitely until interrupted (e.g., Ctrl+C)
        httpd.serve_forever()
        
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
