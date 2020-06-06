import http.server
import socketserver
import ssl                                                      #   For future implementation with Openssl

PORT = 8080                                                     #   Define the standard port
IP = 'localhost'
Request = http.server.SimpleHTTPRequestHandler                  #   Simple http request handler, it commits all files and directories within the SelfHost.py folder

with socketserver.TCPServer((IP, PORT), Request) as httpd:      #   ("ip address", desired port), call the resquests from files
    print("Running @ ",IP,':',PORT)                             #   Simply outputs on terminal the port that the server is operating
    httpd.serve_forever()                                       #   Method that simply begins listening and responding to incoming requests