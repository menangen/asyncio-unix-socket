from os import environ
import signal

from asyncio import get_event_loop


class UnixAsyncSocket:

    socket = environ.get("GAME_SOCKET") or "/tmp/gameserver"

    def __init__(self):
        self.task = None

        self.loop = get_event_loop()
        print("Creating event loop...")

        def ask_exit():
            print("Exit signal")
            self.loop.stop()

        for signame in {'SIGINT', 'SIGTERM'}:
            self.loop.add_signal_handler(getattr(signal, signame), ask_exit)

    def start_task(self, Task, data):
        self.task = self.loop.create_task(Task(self.loop, data)) if data else self.loop.create_task(Task)

        self.loop.run_forever()

    def start_server_task(self, Task, handler):
        unix_server = Task(handler, path=UnixAsyncSocket.socket, loop=self.loop)

        self.loop.create_task(unix_server)

        print("Open Unix socket with Server.")
        self.loop.run_forever()
