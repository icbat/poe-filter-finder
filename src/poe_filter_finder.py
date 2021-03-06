import os
import urllib.request


def find_poe_directory(os_path=os.path):
    user_home_directory = os_path.expanduser("~")
    install_path = user_home_directory + "/Documents/My Games/Path of Exile/"
    print("Checking for Path at path " + install_path)
    if os_path.isdir(install_path):
        print("Found it at " + install_path)
        return install_path
    else:
        raise FileNotFoundError("Couldn't find your Path of Exile installation. Checked at " + install_path)


def find_filters():
    filters = [
        "https://gist.githubusercontent.com/icbat/a2376c23dbfca3f92bbb/raw/0201d153705b2c86fef31a3d93d7d71dae782397/icbat-loot.filter"]
    return filters


def download_filters_to(urls, target_directory, urllib_request=urllib.request):
    for url in urls:
        filename = get_filename(url)
        print("  Grabbing " + filename + " from " + url)
        urllib_request.urlretrieve(url, target_directory + filename)
        print("  Successfully installed " + filename)


def get_filename(url):
    split = str(url).split("/")
    parts = len(split)

    return split[parts - 1]


if __name__ == "__main__":
    print("Finding your Path of Exile install")
    install_directory = find_poe_directory()

    print("Finding Filters")
    filters = find_filters()

    print("Downloading filter to there")
    download_filters_to(filters, install_directory)

    print("BOOM! Filters are installed!")
    print("In Path of Exile, open Options, navigate to the UI Tab and scroll to the bottom to choose one")
    input("Press enter to exit")
