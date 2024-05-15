import os
import re

file_path = './mds.txt'
path = 'mdDocumentation'
# 获取指定目录中的文件和目录列表，只包括以 .md 结尾的文件
entries = [entry for entry in os.listdir(path) if entry.endswith('.md')]
print(entries)
for entry in entries:
    with open(path + '/' + entry, 'r',encoding='utf-8') as file:
        file_content = file.read()
        print(file_content)
        author_match = re.search(r'\*\*作者\*\*：\[(.*?)\]', file_content)# 正则匹配,提取作者信息
        author_name = ""
        if author_match:
            author_name = author_match.group(1)
            print(author_name)
        else:
            
            print("未找到作者信息")
            # 写入作者信息和文件名到文件
        with open(file_path, 'w',encoding='utf-8') as file:
            for entry in entries:
                file.write( entry + " #" +author_name  +'\n')  # 添加换行符确保每个条目在新的一行
# 指定文件路径



