import http.server
import socketserver
import os

PORT = 8080
CALLBACK_URL = f'http://localhost:{PORT}/'

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve index.html for root and OAuth callback (/?code=...)
        clean_path = self.path.split('?')[0]
        if clean_path in ('/', '/index.html'):
            try:
                with open('index.html', 'r', encoding='utf-8') as f:
                    content = f.read()
                # Hardcode the callback URL so it matches the APS app registration
                content = content.replace(
                    "window.location.origin + window.location.pathname.replace(/\\/index\\.html$/, '').replace(/\\/$/, '')",
                    f"'{CALLBACK_URL}'"
                )
                encoded = content.encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(encoded)))
                self.end_headers()
                self.wfile.write(encoded)
            except FileNotFoundError:
                self.send_error(404, 'index.html not found')
        else:
            super().do_GET()

    def log_message(self, format, *args):
        print(f'{self.address_string()} - {format % args}')

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    httpd.allow_reuse_address = True
    print(f'Serving at http://localhost:{PORT}')
    print(f'Callback URL: {CALLBACK_URL}')
    httpd.serve_forever()
