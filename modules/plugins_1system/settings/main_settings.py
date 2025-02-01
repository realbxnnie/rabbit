import time
import os 
import sys

from pathlib import Path


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Config:
    version = "0.10"
    prefix = open("config/prefix.txt", "r").read()
    showlinks = open("config/links.txt", "r").read()
    cmdrights = "me"
    botmessages = []
    reputation = open("config/reputation.txt", "r").read()
    def restart_userbot():
        cls()
        os.execv(sys.executable, ['python'] + sys.argv)


    def setprefix(newprefix):
        oldprefix = Config.prefix
        if os.path.exists("config/prefix.txt"):
            os.remove("config/prefix.txt")
            Path.touch("config/prefix.txt")
            open("config/prefix.txt", "w").write(newprefix)
        Config.prefix = open("config/prefix.txt", "r").read()

        for i in module_list:
            module_list[i] = module_list[i].replace(oldprefix, newprefix)

    def setrep(newrep):
        if os.path.exists("config/reputation.txt"):
            os.remove("config/reputation.txt")
            Path.touch("config/reputation.txt")
            open("config/reputation.txt", "w").write(newrep)
        Config.reputation = open("config/reputation.txt", "r").read()

    def setlinks(newlinks):
        if os.path.exists("config/links.txt"):
            os.remove("config/links.txt")
            Path.touch("config/links.txt")
            open("config/links.txt", "w").write(newlinks)
        Config.reputation = open("config/links.txt", "r").read()



module_list = {}
file_list = {}
