from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import os
import time

# Simple in-memory auction data for demonstration
bids = []

class AuctionHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Serve the main auction HTML page
            self.path = '/templates/auction.html'
        elif self.path.startswith('/static/'):
            # Serve static files (e.g., CSS)
            self.path = self.path
        else:
            # Fallback to a 404 page
            self.send_error(404, "File not found")
            return

        # Serve the requested file
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/bid':
            # Handle bid submissions
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            bid = json.loads(post_data)

            # Record the bid
            bids.append({"user": bid["user"], "amount": float(bid["amount"]), "timestamp": int(time.time())})

            # Respond with the highest bid in JSON format
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            highest_bid = max(bids, key=lambda x: x['amount'])
            self.wfile.write(json.dumps({"status": "success", "highest_bid": highest_bid}).encode())
        else:
            self.send_error(404, "Invalid endpoint")

if __name__ == '__main__':
    # Set the current working directory to serve files
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Start the server
    server = HTTPServer(('0.0.0.0', 8080), AuctionHandler)
    print("Starting Viral Bitcoin Auction server on port 8080...")
    server.serve_forever()