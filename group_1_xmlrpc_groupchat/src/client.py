import subprocess
import xmlrpc.client
from os import system, name
import time
import threading
from config import *
import random
import os
import sys

def cls1():
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')

name = ""
temp_messages = []
proxy = xmlrpc.client.ServerProxy("http://{}:{}/".format(IP, PORT))
status = False

def check_messages(proxy):
    global temp_messages
    global status
    while True:
        time.sleep(1)
        data = proxy.send_message_list()
        if data != temp_messages:
            for d in data:
                if d not in temp_messages:
                    temp_messages.append(d)
                    print(f"\n{d[:int(len(d)-4)]}")

def question_for_message():
    while True:
        msg = input()
        if msg != "":
            id_of_message = random.randint(1000, 9999)
            messages_totais = proxy.send_message(msg+str(id_of_message), name)

def main():
    global name
    cls1()
    print("Welcome to group chat server \n\n")
    name = input("Name?: ")
    func = threading.Thread(target=check_messages, args=(proxy,))
    func.start()
    while True:
        if status == False:
            question_for_message()
            print(CURSOR_UP_ONE + ERASE_LINE + inp)

if __name__ == "__main__":
    print("Connecting to the server...")
    main()
