#!/usr/bin/env python3

# code from lab session

import socket, time, sys

#define global address and buffer size
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

#get ip
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

def main():
  #QUESTION 6 ADDRESS
  extern_host = "www.google.com"
  extern_port = 80

  #create socket
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
    print("Starting proxy server")
    #allow reused addresses, bind, and set to listening mode
    proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    proxy_start.bind((HOST, PORT))
    proxy_start.listen(1)

    while True:
      #connect proxy_start
      conn, addr = proxy_start.accept()
      print("Connected by", addr)

      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
        print("Connecting to Google")
        remote_ip = get_remote_ip(extern_host)

        #connect proxy_end
        proxy_end.connect((remote_ip, extern_port))

        #send data
        send_full_data = conn.recv(BUFFER_SIZE)
        print(f"Sending received data {send_full_data} to google")
        proxy_end.sendall(send_full_data)

        #remember to shut down
        proxy_end.shutdown(socket.SHUT_WR) #shutdown() is different than close()

        data = proxy_end.recv(BUFFER_SIZE)
        print(f"Sending received data {data} to client")
        #send data back
        conn.send(data)
      
      conn.close()

if __name__ == "__main__":
  main()
