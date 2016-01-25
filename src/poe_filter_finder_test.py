from poe_filter_finder import get_filename, find_poe_directory


def get_filename_test_happy():
    filename = "filename.txt"
    url = "http://www.example.com/" + filename
    assert get_filename(url) == filename


def get_filename_test_empty_string():
    empty_string = ""
    assert get_filename(empty_string) == empty_string


def get_filename_test_no_split():
    url = "text_with_no_slash"
    assert get_filename(url) == url


def get_filename_test_just_slashes():
    url = "////"
    assert get_filename(url) == ""


def find_poe_directory_test_happy():
    user_path = "c:/expanded_user/"

    poe_directory = find_poe_directory(MockOsPath(user_path, True))

    assert poe_directory == user_path + "/Documents/My Games/Path of Exile/"

def find_poe_directory_test_throws_when_cant_find_directory():
    user_path = "not a path at all/"

    try:
        poe_directory = find_poe_directory(MockOsPath(user_path, False))
        assert False
    except:
        pass


class MockOsPath:
    def __init__(self, expandusr_response, isdir_response):
        self.expandusr_response = expandusr_response
        self.isdir_response = isdir_response

    def expanduser(self, path):
        return self.expandusr_response

    def isdir(self, path):
        return self.isdir_response
