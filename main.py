import os

parent_dir_path = './'
total_rows = 0
total_files = 0


def walkInDir(dir_path):
    global total_rows, total_files
    for f_path, dirs, files in os.walk(dir_path):
        for dir in dirs:
            walkInDir(os.path.join(dir_path, dir))
        for file in files:
            if file.split(".")[-1] in ['py','java']:
                file_path = os.path.join(dir_path, file)
                code_rows = getCodeQuantity(file_path)
                if code_rows != 0:
                    total_files += 1
                    print('{} has {} rows code!'.format(file_path, code_rows))
                    total_rows += code_rows


def getCodeQuantity(file_path):
    global total_files
    try:
        with open(file_path, encoding="utf-8") as f:
            content = f.readlines()
            return len(content)
    except Exception as e:
        return 0


if __name__ == '__main__':
    walkInDir(parent_dir_path)
    print("一共有{}个有效文件,共计{}行代码！".format(total_files,total_rows))
