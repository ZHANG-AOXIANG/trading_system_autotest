# Abstract: Read yaml file through PyYAML library
# Time: 2023-11-28
# Authour: Aoxiang Zhang

import yaml


class GetConf:
    def __init__(self):
        file_path = "../config/environment.yaml"
        with open(file_path, "r", encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_username(self):
        return self.env["username"]

    def get_password(self):
        return self.env["password"]


if __name__ == "__main__":
    print(GetConf().get_username())
    print(GetConf().get_password())
