from poe_filter_finder import get_filename


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

