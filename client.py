from asyncio import coroutine, open_unix_connection, sleep
from async_socket import UnixAsyncSocket


@coroutine
async def write_socket(loop, byte_message):
    try:
        reader_sock, writer_sock = await open_unix_connection(path=UnixAsyncSocket.socket, loop=loop)

        print("Open unix socket with Client.")

        writer_sock.write(byte_message)

        writer_sock.close()

        print("Data", byte_message, "sent, stopping loop")
        loop.stop()

    except ConnectionRefusedError:
        print("No socket opened by server")
    except FileNotFoundError:
        print("Socket is not exists")


@coroutine
async def check_task(loop, data):
    while True:
        loop.create_task(write_socket(loop, data))

        await sleep(1, loop=loop)


if __name__ == '__main__':
    Socket = UnixAsyncSocket()

    data_to_write = bytes(
                "menangen",
                encoding="ascii"
            )
    server = Socket.start_task(check_task, data_to_write)
