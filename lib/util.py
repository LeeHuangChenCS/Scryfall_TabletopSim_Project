import os

# generate all the directories needed for the given path (helper function)
def generateDirectories(path):
    #folders = path.split("/")
    path = os.path.normpath(path)
    folders = path.split(os.sep)
    #folders = os.path.split(path)
    print(folders)

    curdir = ""
    prevFolder = ""
    for folder in folders:
        print(folder)
        if len(folder.strip())>0:
            prevFolder = curdir
            curdir = os.path.join(curdir, folder)
            if not os.path.exists(curdir):
                # print curdir
                # os.chmod(prevFolder,stat.S_IWRITE)
                os.mkdir(curdir)