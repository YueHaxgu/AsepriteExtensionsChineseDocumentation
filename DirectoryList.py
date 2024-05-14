import os


path = 'mdDocumentation'
# 获取指定目录中的文件和目录列表，只包括以 .md 结尾的文件
entries = [entry for entry in os.listdir(path) if entry.endswith('.md')]
print(entries)
# 指定文件路径
file_path = './mds.txt'


with open(file_path, 'w',encoding='utf-8') as file:
    for entry in entries:
        file.write(entry + '\n')  # 添加换行符确保每个条目在新的一行