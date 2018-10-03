"""
    author: RealgodJJ
    function: Password Tool
    version: 1.0
    date: 2018/10/3
"""


class PasswordTool:
    """
        密码工具类
    """

    def __init__(self, password):
        self.password = password
        self.strength = 0

    def process_password(self):
        if len(self.password) >= 8:
            self.strength += 1
        else:
            print("密码的长度未超过8位！")

        if self.check_number_exist():
            self.strength += 1
        else:
            print("密码不包含数字！")

        if self.check_alphabet_exist():
            self.strength += 1
        else:
            print("密码不包含字母！")

    def check_number_exist(self):
        has_number = False
        for value in self.password:
            if value.isnumeric():
                has_number = True
                break
        return has_number

    def check_alphabet_exist(self):
        has_alphabet = False
        for value in self.password:
            if value.isalpha():
                has_alphabet = True
                break
        return has_alphabet
