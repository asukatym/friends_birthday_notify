import subprocess
import time
proc=subprocess.Popen(['python3', 'app.py'])
from main import Birthday
Birthday = Birthday()
Birthday.check_birthday()
Birthday.line_notify()
Birthday.notify()
proc.kill()
