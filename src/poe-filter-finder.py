import os
import urllib.request

def findPathInstallDirectory():
    userHome = os.path.expanduser("~")
    installPath = userHome + "/Documents/My Games/Path of Exile/"
    print("Checking for Path at path " + installPath)
    if os.path.isdir(installPath):
        print("Found it at " + installPath)
        return installPath
    else:
        raise FileNotFoundError("Couldn't find your Path of Exile installation. Checked at " + installPath)

def findFilters():
    filters = []
    filters.append("https://gist.githubusercontent.com/icbat/a2376c23dbfca3f92bbb/raw/dbd42a0f15b66054dd94d9eff7a5aac05328bb16/icbat-loot.filter")
    return filters

def downloadAllFiltersTo(filters, installDirectory):
    for url in filters:
        urllib.request.urlretrieve(url, installDirectory + "test.filter")

print("Finding your Path of Exile install")
installDirectory = findPathInstallDirectory()

print("Finding Filters")
filters = findFilters()

print("Downloading filter to there")
downloadAllFiltersTo(filters, installDirectory)

print("BOOM! Go get loot with prettier colors.")
input("Press enter to exit")
