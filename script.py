import http.server
import socketserver
import os

# Define the port and directory where images are stored
PORT = 5000
DIRECTORY = "static/images"  # Ensure your image is inside this folder

# Change the working directory to serve images
os.chdir(DIRECTORY)

# Create a simple HTTP server
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://127.0.0.1:{PORT}/")
    print(f"Access your image at: http://127.0.0.1:{PORT}/cat.jpg")
    
    # Keep the server running until manually stopped
    httpd.serve_forever()

