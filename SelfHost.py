import http.server
import socketserver

PORT = 8080                                                     #   Define the standard port
Handler = http.server.SimpleHTTPRequestHandler                  #   Simple http request handler, it commits all files and directories within the SelfHost.py folder

with socketserver.TCPServer(("", PORT), Handler) as httpd:      #   ("ip address", desired port), call the resquests from files
    print("Running @ ", PORT)                                   #   Simply outputs on terminal the port that the server is operating
    httpd.serve_forever()                                       #   Method that simply begins listening and responding to incoming requests