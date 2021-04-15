import os
import shutil
import subprocess
import time
from pathlib import Path
import sys

if __name__ == '__main__':
    subprocess.Popen(["dist\\CopyExe.exe","./","updateFile","file_md5.dat", "file_md55.dat", 'CopyExe.exe', 'main.exe'])
    print("start copy exe")
    time.sleep(5)