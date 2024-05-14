import os


path = 'mdDocumentation'
# 获取指定目录中的文件和目录列表
entries = os.listdir(path)
print(entries)

# 指定文件路径
file_path = './mds.txt'


with open(file_path, 'w',encoding='utf-8') as file:
    for entry in entries:
        file.write(entry + '\n')  # 添加换行符确保每个条目在新的一行