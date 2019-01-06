from asyncio import coroutine, get_event_loop, start_unix_server

from async_socket import UnixAsyncSocket


@coroutine
async def handle(reader, writer):
    print("Handling connection")

    data = await reader.read(512)

    print(data, "received")


if __name__ == '__main__':

    Socket = UnixAsyncSocket()

    unix_server = Socket.start_server_task(start_unix_server, handle)
