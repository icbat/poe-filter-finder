import os
import urllib.request


def find_poe_directory():
    user_home_directory = os.path.expanduser("~")
    install_path = user_home_directory + "/Documents/My Games/Path of Exile/"
    print("Checking for Path at path " + install_path)
    if os.path.isdir(install_path):
        print("Found it at " + install_path)
        return install_path
    else:
        raise FileNotFoundError("Couldn't find your Path of Exile installation. Checked at " + install_path)


def find_filters():
    filters = [
        "https://gist.githubusercontent.com/icbat/a2376c23dbfca3f92bbb/raw/dbd42a0f15b66054dd94d9eff7a5aac05328bb16/icbat-loot.filter"]
    return filters


def download_filters_to(filters, target_directory):
    for url in filters:
        filename = get_filename(url)
        print("  Grabbing " + filename + " from " + url)
        urllib.request.urlretrieve(url, target_directory + filename)
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
