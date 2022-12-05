import sys
import subprocess
import shutil
import os

# shellCmd :: Str -> (Int, Str, Str)
def mlc_shellCmd(args):
    try:
        x = subprocess.run(args, capture_output=True)
    except FileNotFoundError:
        return (1, "Command not found", "")
    return (x.returncode, x.stderr, x.stdout)


# writeCreate :: Str -> Filename -> ()
def mlc_writeCreate(text, filename):
    with open(filename, "w") as f:
        f.write(text)

# writeAppend :: Str -> Filename -> ()
def mlc_writeAppend(text, filename):
    with open(filename, "a") as f:
        f.write(text)

# read :: Filename -> Str
def mlc_read(filename):
    with open(filename, "r") as f:
        return f.read()

# cd :: Filename -> ()
def mlc_cd(path):
    os.chdir(path)

def mlc_copyFile(path1, path2):
    shutil.copyfile(path1, path2)

# mkdir :: Filename -> ()
def mlc_mkdir(path):
    os.mkdir(path)

# pwd :: () -> String
def mlc_pwd():
    return os.getcwd()

# mv :: Filename -> Filename -> ()
def mlc_mv(path1, path2):
    os.rename(path1, path2)
