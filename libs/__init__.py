import socket
class Banner:
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def _get_Banner(self):
        try:
            self.sock.connect((self.host,self.port))
            if(self.port == 80 or 8080):
                self.sock.sendall(b"HEAD / HTTP/1.1\r\nHost: %b\r\n\r\n" % self.host.encode())
            try:
                data = self.sock.recv(1024)
                return data.decode().strip()
            except ():
                return "No Banner Available"
            
        except():
            return "Port is not Open"

