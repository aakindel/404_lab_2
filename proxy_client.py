#!/usr/bin/env python3

# code from lab session

import socket 

#define address, buffer size
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024


payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
  #create socket, connect and receive data
  try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    s.sendall(payload.encode())
    s.shutdown(socket.SHUT_WR) #shutdown() is different from close()

    full_data = s.recv(BUFFER_SIZE)
    print(full_data)

  except Exception as e:
    print(e)
  finally:
    #remember to close!!
    s.close()

def main(): 
  connect((HOST, PORT))

if __name__ == "__main__":
  main()
