import json
import time

import os

import glob
import importlib

from pyrogram import *
from pyfiglet import *
from pystyle import Colorate, Colors
from colorama import Fore, Back

class ModuleManager:
    def __init__(self):
        self.modules = {

        }

        def add(name, version, callback):
            new = {}
            for i, v in self.modules.items():
                new[i] = v

                new[name] = {
                    "version": version,
                    "callback": callback
                }

                self.modules.update(new)

                print(f"[MODULEMANAGER]: Loaded module {name}")
                print(self.modules)

        self.add = add

moduleMgr = ModuleManager()

class Rabbit:
    def __init__(self):
        try:
            print(f"{Colorate.Vertical(Colors.white_to_black, figlet_format("Rabbit"))}")
            print("A powerful Telegram Userbot.")
            print("\n")
            print(f"{Colorate.Vertical(Colors.red_to_yellow, "----------- OUTPUT ---------")}")
            self.config = json.loads(open("private.json", "r+").read())

            self.api_id = self.config["api_id"]
            self.api_hash = self.config["api_hash"]
            self.phone_number = self.config["phone_number"]
            self.username = self.config["username"]

            if self.api_id == "":
                self.api_id = int(input(f"{Fore.BLUE}Enter your API ID: {Fore.GREEN}"))
                self.config["api_id"] = self.api_id
                json.dump(self.config, open("private.json", "w+"))
            
            if self.api_hash == "":
                self.api_hash = input(f"{Fore.BLUE}Enter your API Hash: {Fore.GREEN}")
                self.config["api_hash"] = self.api_hash
                json.dump(self.config, open("private.json", "w+"))


            if self.phone_number == "":
                self.phone_number = input(f"{Fore.BLUE}Enter your Phone Number: {Fore.GREEN}")
                self.config["phone_number"] = self.phone_number
                json.dump(self.config, open("private.json", "w+"))

            if self.username == "":
                self.username = input(f"{Fore.BLUE}Enter your username: {Fore.GREEN}")
                self.config["username"] = self.username
                json.dump(self.config, open("private.json", "w+"))

            print(Fore.WHITE)

            self.client = Client(name=self.username, api_id=self.api_id, api_hash=self.api_hash, phone_number=self.phone_number, plugins=dict(root="modules"), device_model="RabbitUserbot")
            self.modules = glob.glob("modules/*")

            self.client.run()
        
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Exiting Rabbit...{Fore.WHITE}")

userbot = Rabbit()