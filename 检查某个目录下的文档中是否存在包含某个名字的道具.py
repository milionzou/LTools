import os
def get_files_by_suffix(path, suffixes=("txt", "xml","xlsx"), traverse=True):
    """从path路径下，找出全部指定后缀名的文件
    :param path: 根目录
    :param suffixes: 指定查找的文件后缀名
    :param traverse: 如果为False，只遍历一层目录
    :return:
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_suffix = os.path.splitext(file)[1][1:].lower()   # 后缀名
            if file_suffix in suffixes:
                file_list.append(os.path.join(root, file))
        if not traverse:
            return file_list

    return file_list


if __name__ == '__main__':
    keyword = "哈哈"
    files = get_files_by_suffix("D:\\TEST")
    print(files)

    for file in files:

        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().encode('utf-8').decode()
            print(content)
            position = content.find(keyword)

            if position != -1:
                print("Find in {0}".format(file))
                start = position - 100 if position - 100 > 0 else 0
                end = position + 100 if position + 100 < len(content) else len(content)
                print(content[start:end])
                print("_" * 100)