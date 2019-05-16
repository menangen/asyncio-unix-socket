import socket


def httpHandler(tcpSocket):

        proto = b"HTTP/1.1 200 OK\n"
        body = b"<html><body>Hello from Python 3</body></html>\n"
        headers = f"Content-Type: text/html; encoding=ascii\nContent-Length: {len(body)}\nConnection: close\n"

        tcpSocket.send(proto)
        tcpSocket.send(bytes(headers, encoding='ascii'))
        tcpSocket.send(b'\n')  # to separate headers from body
        tcpSocket.send(body)

socketConfig = ("127.0.0.1", 8080)

tcpSocket = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_STREAM)

tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(socketConfig)
print(tcpSocket)

tcpSocket.listen()

connection, address = tcpSocket.accept()
print("Accepting from", address)

data = connection.recv(128)

print("Data:")
print(data.decode(encoding="ascii"))

httpHandler(connection)

connection.close()
tcpSocket.close()
