import signal
from asyncio import coroutine, get_event_loop, start_unix_server


@coroutine
async def handle(reader, writer):
    print("Handling connection")

    data = await reader.read(512)

    print(data, "received")


if __name__ == '__main__':

    loop = get_event_loop()
    print("Creating event loop...")

    unix_server = start_unix_server(handle, path="/tmp/gameserver", loop=loop)
    print("Open unix socket with Server.")

    server = loop.run_until_complete(unix_server)

    def ask_exit():
        print("Got signal exit")
        loop.stop()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), ask_exit)

    loop.run_forever()
