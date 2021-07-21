import os
import sys


def restart_application(self):
    self.master.destroy()
    python = sys.executable
    os.execl(python, "../executable.py", *sys.argv)
