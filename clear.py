import os
import sys


def clear():
    new_handler = open('/tmp/out.log', 'w')
    old_handler = sys.stdout
    sys.stdout = new_handler
    os.system('clear')
    sys.stdout = old_handler
