# coding=utf-8
"""
    author: RealgodJJ
    function: Judge the password strength
    version: 1.0
    date: 2018/10/2
"""


def check_number_exist(password):
    has_number = False
    for value in password:
        if value.isnumeric():
            has_number = True
            break
    return has_number


def check_alphabet_exist(password):
    has_alphabet = False
    for value in password:
        if value.isalpha():
            has_alphabet = True
            break
    return has_alphabet


def main():
    try_times = 5

    while try_times > 0:
        password = input("请输入设置的密码：\n")
        strength = 0

        if len(password) >= 8:
            strength += 1
        else:
            print("密码的长度未超过8位！")

        if check_number_exist(password):
            strength += 1
        else:
            print("密码不包含数字！")

        if check_alphabet_exist(password):
            strength += 1
        else:
            print("密码不包含字母！")

        if strength == 3:
            print("密码格式设置正确！\n")
            break
        else:
            print("密码设置不符合规则！\n")
            try_times -= 1

    if try_times == 0:
        print("尝试次数过多，密码设置失败！")


if __name__ == '__main__':
    main()
