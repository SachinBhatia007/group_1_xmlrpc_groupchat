from xmlrpc.server import SimpleXMLRPCServer
from config import *

class chat_server:
    def __init__(self, arg):
        self.arg = arg
        self.messages = []

    def send_message(self, msg, author):
        if msg != "":
            self.messages.append("[{}] - {}".format(author, msg))
            return self.messages

    def send_message_list(self):
        return self.messages

server = SimpleXMLRPCServer((IP, PORT))
print(f"Open connections on the port {IP}:{PORT}...\n")
server.register_instance(chat_server("a"))
print("Server ready to receive messages...")
server.serve_forever()