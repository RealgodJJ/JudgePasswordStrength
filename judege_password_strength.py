# coding=utf-8
"""
    author: RealgodJJ
    function: Judge the password strength
    version: 1.0
    date: 2018/10/2
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


def main():
    try_times = 5

    while try_times > 0:
        password = input("请输入设置的密码：\n")
        # 实例化对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        file = open("password.txt", "a")
        file.write("密码：{}   强度：{}\n".format(password, password_tool.strength))
        file.close()

        # style 1
        print("====== Style 1 ======")
        file = open("password.txt", "r")
        content = file.read()
        print(content)
        file.close()

        # style 3
        print("====== Style 2 ======")
        file = open("password.txt", "r")
        for item, line in enumerate(file.readlines()):
            print("{}.{}".format(item + 1, line))
        file.close()

        if password_tool.strength == 3:
            print("密码格式设置正确！\n")
            break
        else:
            print("密码设置不符合规则！\n")
            try_times -= 1

    if try_times == 0:
        print("尝试次数过多，密码设置失败！")


if __name__ == '__main__':
    main()
