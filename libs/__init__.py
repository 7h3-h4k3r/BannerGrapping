import socket
import ssl
class Banner:
    def __init__(self,host,port,timeout=3.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        
    def _get_Banner(self):
        try:
    
            addr_info = socket.getaddrinfo(
                self.host,
                self.port,
                family=socket.AF_UNSPEC,
                type=socket.SOCK_STREAM
            )
        except socket.gaierror as e:
            return f"DNS resolution failed: {e}"

        for family, socktype, proto, canonname, sockaddr in addr_info:
            sock = None
            try:
                sock = socket.socket(family, socktype, proto)
                sock.settimeout(self.timeout)
                sock.connect(sockaddr)
                if self.port == 443:
                    context = ssl.create_default_context()
                    sock = context.wrap_socket(sock, server_hostname=self.host)
    
                if self.port in (80, 8080):
            
                    host_header = f"[{self.host}]" if family == socket.AF_INET6 and ":" in self.host else self.host
                    request = f"HEAD / HTTP/1.1\r\nHost: {host_header}\r\n\r\n".encode()
                    sock.sendall(request)

                data = sock.recv(1024)
                if not data:
                    return "No banner available (empty response)"
                return data.decode(errors="ignore").strip()

            except socket.timeout:
                continue 
            except ConnectionRefusedError:
                continue  
            except Exception:
                continue
            finally:
                if sock:
                    sock.close()

            return f"Port {self.port} is closed, filtered, or host unreachable on all resolved addresses"

