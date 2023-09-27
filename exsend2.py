import socket as s

class UDP():
    def __init__(self, log=False):
        """Creates an UDP server or client"""
        self.__logging=False
        self.__soc = s.socket(s.AF_INET, s.SOCK_DGRAM)
        self.__bound = False

    def Send(self, data:str, ip: str, port: int):
        """Sends data to remote host"""
        
        self.__soc.sendto(bytes(str(data), "utf-8"), (ip, port))
        

    def Receive(self, port: int, timeout: float = 0):
        """Receives UDP packet and returns a string, None if no packets were received."""
        if timeout != 0: self.__soc.settimeout(timeout)
        if not self.__bound:
            self.__soc.bind(('', port))
            self.__bound = True

        __data, __addr = self.__soc.recvfrom(port)
        return bytes(__data).decode("utf-8"), __addr


class TCP():
    def __init__(self, log=False):
        """Creates a TCP server or a TCP client."""
        
        self.__tcpdata = ""
        self.buffer_size = 1024
        self.__logging = log
    
    def Connect(self, remoteip: str, port: int):
        """Creates TCP connection to the given host on the given port."""

        global soc
        soc = s.socket(s.AF_INET, s.SOCK_STREAM)
        soc.connect((remoteip, port))
        if self.__logging: print("connected")

    def Close(self):
        """Closes the existing TCP connection."""
        soc.close()
    

    def Listen(self, port: int, timeout: int = 0) -> None:
        """Starts listening on the given port"""

        global soc
        start_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        start_socket.bind(("", port))
        start_socket.listen()
        if timeout != 0: start_socket.settimeout(timeout)
        soc, addr = start_socket.accept()
        if self.__logging == True:
            print("Connected to: " + str(addr))
        
    def Receive(self, timeout: float = 0) -> str:
        """Receives TCP packet and returns a string, None if no packets were received."""
        if timeout != 0: soc.settimeout(timeout)
        data = soc.recv(self.buffer_size)
        if data != b'':
            return bytes(data).decode("utf-8")

    def Send(self, data: str):
        """Sends data to the remote host"""
        soc.send(bytes(str(data), 'utf-8'))
    

# How to use
#----------------------------------------------------------------
        #UDP server example:
        #udp = UDP()
        #print(udp.Receive())

        #UDP client example:
        #udp = UDP()
        #udp.Send("Hello world")


        # TCP server example:
        # tcp = TCP()
        # tcp.Listen(2021)         
        # print( tcp.Receive() )
        
        
        # TCP client example:
        # tcp = TCP()
        # tcp.connect("192.168.1.2", 2021)
        # tcp.Send("Hello World")
        # tcp.Close()