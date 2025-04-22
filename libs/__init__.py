import socket
import colorama

class Banner:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def _get_Banner(self):
        try:
            self.sock.connect((self.host,self.port))
            data = self.sock.recv(1024)
            print(data.decode())
        except:
            print("Connection is Not happen")
    
obj = Banner('34.111.55.4',443)._get_Banner()

HEAD / HTTP/1.0
