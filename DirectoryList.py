import os
import re

file_path = './mds.txt'
path = 'mdDocumentation'
# 获取指定目录中的文件和目录列表，只包括以 .md 结尾的文件
entries = [entry for entry in os.listdir(path) if entry.endswith('.md')]
print(entries)
with open(file_path, 'w',encoding='utf-8') as file:
    file.write("")  #初始化文件内容为空
for entry in entries:
    with open(path + '/' + entry, 'r',encoding='utf-8') as file:
        file_content = file.read()
        print(file_content)
        
        author_name = ""
        author_href =""
        pattern = r'\*\*作者\*\*：\[(.*?)\]\((.*?)\)'

        # 使用正则表达式进行匹配
        matches = re.findall(pattern, file_content)
        if matches:
            for match in matches:
                print("作者：", match[0])
                print("链接：", match[1])
                author_name = match[0]
                author_href = match[1]
                with open(file_path, 'a',encoding='utf-8') as file:
                    file.write( entry + " #" +author_name  + " @" + author_href + '\n' )  # 添加换行符确保每个条目在新的一行
        else:
            
            print("未找到作者信息")
            # 写入作者信息和文件名到文件
        




