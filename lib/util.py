import os

# generate all the directories needed for the given path (helper function)
def generateDirectories(path):
    folders = path.split("/")
    curdir = ""
    prevFolder = ""
    for folder in folders:
        prevFolder = curdir
        curdir = os.path.join(curdir, folder)
        if not os.path.exists(curdir):
            # print curdir
            # os.chmod(prevFolder,stat.S_IWRITE)
            os.mkdir(curdir)