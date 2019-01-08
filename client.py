from asyncio import coroutine, open_unix_connection, sleep
from async_socket import UnixAsyncSocket
import socket  # aiodns


@coroutine
async def write_socket(loop, data):
    try:
        reader_sock, writer_sock = await open_unix_connection(path=UnixAsyncSocket.socket, loop=loop)

        print("Open unix socket with Client.")

        byte_message = data["message"] + str(data["counter"]).encode("ascii")

        writer_sock.write(byte_message)
        print("Data", byte_message, "sent")

        writer_sock.close()

        if data["counter"] == 50:
            print("Stopping loop")
            loop.stop()
        else:
            data["counter"] += 1
            print("Increse Counter = ", data['counter'])

    except ConnectionRefusedError:
        print("No socket opened by server")
    except FileNotFoundError:
        print("Socket is not exists")


@coroutine
async def dns(loop, hostname):
    # resolver = aiodns.DNSResolver(loop=loop)
    # result = await resolver.query(hostname, "A")
    #
    # print([record.host for record in result])
    # native async DNS resolver
    res = await loop.getaddrinfo(hostname, 80, proto=socket.IPPROTO_UDP)
    for record in res:
        print(record[4][0])


@coroutine
async def check_task(loop, message):
    data = {
        "counter": 0,
        "message": message
    }

    while True:
        loop.create_task(dns(loop, "gameserver.novikova.us"))
        loop.create_task(write_socket(loop, data))

        await sleep(15, loop=loop)


if __name__ == '__main__':
    Socket = UnixAsyncSocket()

    data_to_write = bytes(
                "packet=",
                encoding="ascii"
            )
    server = Socket.start_task(check_task, data_to_write)
