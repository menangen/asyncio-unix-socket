import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 5001

udpSocket = socket.socket(
            socket.AF_INET,     # Internet
            socket.SOCK_DGRAM)  # UDP

print(udpSocket)

udpSocket.bind((UDP_IP, UDP_PORT))

res: int = udpSocket.sendto(
            b"Hello from Python3",
            ("127.0.0.1", 5000)
        )

print(res)

