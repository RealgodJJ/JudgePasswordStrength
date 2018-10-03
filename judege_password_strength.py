# coding=utf-8
"""
    author: RealgodJJ
    function: Judge the password strength
    version: 1.0
    date: 2018/10/2
"""
from file_tool import FileTool
from password_tool import PasswordTool


def main():
    try_times = 5
    file_path = "password.txt"
    # 实例化File_Tool类对象
    file_tool = FileTool(file_path)

    while try_times > 0:
        password = input("请输入设置的密码：\n")
        # 实例化PasswordTool类对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        # 文件写操作
        line = "密码：{}   强度：{}\n".format(password, password_tool.strength)
        file_tool.write_to_file(line)

        # 文件读操作
        lines = file_tool.read_from_file()
        for item, line in enumerate(lines):
            print("{}.{}".format(item + 1, line))

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
