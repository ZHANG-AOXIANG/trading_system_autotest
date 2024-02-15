# @PURPOSE: Login in the trading website
# @AUTHOR: Aoxiang Zhang
# @TIME: 16:31 2024/2/3 UTC+8


from config import WebdriverConfig


class LoginBase:
    def login_input(self, input_placeholder):
        """
        input for USER NAME and PASSWORD
        :param input_placeholder:
        :return:
        """

        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self, button_name):
        '''
        login in button
        :param button_name:
        :return:
        '''
        return "//span[text()='" + button_name + "']/parent::button"


if __name__ == "__main__":
    print(LoginBase().login_input("用户名"))
    print(LoginBase().login_input("密码"))
    print(LoginBase().login_button("登录"))
