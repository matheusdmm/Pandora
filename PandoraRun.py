#   
#        _ __    ,---.      .-._                       _,.---._                  ,---.      
#     .-`.' ,`..--.'  \    /==/ \  .-._  _,..---._   ,-.' , -  `.   .-.,.---.  .--.'  \     
#    /==/, -   \==\-/\ \   |==|, \/ /, /==/,   -  \ /==/_,  ,  - \ /==/  `   \ \==\-/\ \    
#   |==| _ .=. /==/-|_\ |  |==|-  \|  ||==|   _   _\==|   .=.     |==|-, .=., |/==/-|_\ |   
#   |==| , '=',\==\,   - \ |==| ,  | -||==|  .=.   |==|_ : ;=:  - |==|   '='  /\==\,   - \  
#   |==|-  '..'/==/ -   ,| |==| -   _ ||==|,|   | -|==| , '='     |==|- ,   .' /==/ -   ,|  
#   |==|,  |  /==/-  /\ - \|==|  /\ , ||==|  '='   /\==\ -    ,_ /|==|_  . ,'./==/-  /\ - \ 
#   /==/ - |  \==\ _.\=\.-'/==/, | |- ||==|-,   _`/  '.='. -   .' /==/  /\ ,  )==\ _.\=\.-' 
#   `--`---'   `--`        `--`./  `--``-.`.____.'     `--`--''   `--`-`--`--' `--`         
#   
#   VERSION 0.5
#   
#   DO NOT USE IT ON PRODUCTION
#    

import http.server
import socketserver
import socket
import ssl                                                        #   For future implementation with Openssl

PORT      = 8080                                                  #   Define the standard port
HOST      = 'localhost'                                           #   Define the standard host
Request   = http.server.SimpleHTTPRequestHandler                  #   Simple http request handler, it commits all files and directories within the SelfHost.py folder

with socketserver.TCPServer((HOST, PORT), Request) as httpd:      #   ("host/ip address", desired port), call the resquests from files
    
    
    print("Running @ ",HOST,':',PORT)                             #   Simply outputs on terminal the port that the server is operating
    httpd.serve_forever()                                         #   Method that simply begins listening and responding to incoming requests

    while socketserver == True:
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((HOST, PORT))
        listener.listen(1)
        listener.sendall(httpd)

