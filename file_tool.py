"""
    author: RealgodJJ
    function: File Tool
    version: 1.0
    date: 2018/10/3
"""


class FileTool:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_file(self, line):
        file = open(self.file_path, "a")
        file.write(line)
        file.close()

    def read_from_file(self):
        file = open(self.file_path, "r")
        lines = file.readlines()
        file.close()
        return lines