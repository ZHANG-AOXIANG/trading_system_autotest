# Abstract: Read yaml file through PyYAML library
# Time: 2023-11-28
# Authour: Aoxiang Zhang

import yaml


class GetConf:
    def __init__(self):
        file_path = "../config/environment.yaml"
        with open(file_path, "r", encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)

    def get_username(self, user):
        # return self.env["username"]
        return self.env['user'][user]['username']

    def get_password(self, user):
        # return self.env["password"]
        return self.env['user'][user]['password']

    def get_dbConfig(self):
        return self.env["mysql"]

    def get_url(self):
        return self.env["url"]


