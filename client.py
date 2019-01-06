import asyncio


@asyncio.coroutine
async def unix_client():
    print("Creating event loop...")
    loop = asyncio.get_running_loop()

    try:
        # Create a pair of connected sockets.
        reader_sock, writer_sock = await asyncio.open_unix_connection(path="/tmp/gameserver", loop=loop)
        print("Open unix socket with Client.")

        writer_sock.write(bytes(
            "menangen",
            encoding="ascii"
        ))

        writer_sock.close()

    except ConnectionRefusedError:
        print("No socket opened by server")

asyncio.run(unix_client())
