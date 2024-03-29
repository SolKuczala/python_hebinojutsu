#!/usr/bin/env python  
  
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer  
import os  
  
#Create custom HTTPRequestHandler class  
class myRequestHandler(BaseHTTPRequestHandler):  

  #handle GET command  
  def do_GET(self):  
    rootdir = '~/Documents/Outreachy program' #file location  
    try:  
      if self.path.endswith('.html'):  
        f = open(rootdir + self.path) #open requested file  
  
        #send code 200 response  
        self.send_response(200)  
  
        #send header first  
        self.send_header('Content-type','text-html')  
        self.end_headers()  
  
        #send file content to client  
        self.wfile.write(f.read())  
        f.close()  
        return  

    except IOError:  
      self.send_error(404, 'file not found')  

def run():  
  print('http server is starting...')  
  
  #ip and port of servr  
  #by default http server port is 90
  server_address = ('127.0.0.1', 90)  
  httpd = HTTPServer(server_address, myRequestHandler)  
  print('http server is running...')  
  httpd.serve_forever()  

if __name__ == '__main__':  
  run()  