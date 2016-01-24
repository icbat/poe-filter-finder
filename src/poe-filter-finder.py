import os


def findPathInstallDirectory():
    userHome = os.path.expanduser("~")
    installPath = userHome + "/Documents/My Games/Path of Exile"
    print("Checking for Path at path " + installPath)
    if os.path.isdir(installPath):
        print("Found it at " + installPath)
    else:
        raise FileNotFoundError("Couldn't find your Path of Exile installation. Checked at " + installPath)

print("Finding your Path of Exile install")
installDirectory = findPathInstallDirectory()
print("Downloading filter to there")
print("BOOM! Go get loot with prettier colors.")
input("Press enter to exit")
