# @PURPOSE: tools' functions
# @AUTHOR: Aoxiang Zhang
# @TIME: 22:46 2024/5/9 UTC+8
import datetime
import os
import requests


def get_now_time():
    return datetime.datetime.now()


def get_now_date_time_str():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def get_project_path():
    project_name = "trading_system_autotest"
    file_path = os.path.dirname(__file__)
    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


def get_img_path(img_name):
    """
    get the goods image's path
    :param img_name: image file name
    """

    img_dir_name = get_project_path() + sep(['img', img_name], add_sep_before=True)
    return img_dir_name


if __name__ == "__main__":
    img_name = "book.jpeg"
    print(get_project_path())
    print(get_img_path(img_name))
