from asyncio import coroutine, get_event_loop, open_unix_connection, sleep, CancelledError
import signal


@coroutine
async def task(loop):
    try:
        while True:
            print("Running")
            await sleep(1, loop=loop)
    except CancelledError:
        print("Cancelled")

if __name__ == '__main__':

    loop = get_event_loop()
    print("Creating event loop...")

    try:
        client = open_unix_connection(path="/tmp/gameserver", loop=loop)
        print("Open unix socket with Client.")

        reader_sock, writer_sock = loop.run_until_complete(client)

        writer_sock.write(bytes(
            "menangen",
            encoding="ascii"
        ))

        writer_sock.close()

    except ConnectionRefusedError:
        print("No socket opened by server")

    def ask_exit():
        print("Got signal exit")
        loop.stop()

    for signame in {'SIGINT', 'SIGTERM'}:
        loop.add_signal_handler(getattr(signal, signame), ask_exit)

    server = loop.create_task(task(loop))

    loop.run_forever()
