# coding=utf-8
"""
    author: RealgodJJ
    function: Judge the password strength
    version: 1.0
    date: 2018/10/2
"""

def check_number_exist(password):
    for value in password:
        if value.isnumeric():
            return True
    return False


def check_alphabet_exist(password):
    for value in password:
        if value.isalpha():
            return True
    return False

def main():
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
        print("密码格式设置正确！")
    else:
        print("密码设置不符合规则！")

if __name__ == '__main__':
    main()