# -*- coding: UTF-8 -*-
# Author crafteverywhere
# minecraft中文本地化文本更新辅助工具
##############################################
# 使用说明：
# 本脚本使用python3.X编写，运行前请先配置好python3.X环境。
# 本脚本用于检测新旧汉化文本并自动标注变化条目和新增条目。
# 使用前先在脚本同目录位置建立三个文件夹，分别命名为old，new和output
# 将旧版本的en_US.lang和zh_CN.lang丢入old文件夹。
# 将新版本的en_US.lang丢入new文件夹。
# 运行该脚本后，可以在output路径下发现导出的en_US.lang文件，在其基础上可以很方便地更新文本。
# 导出的文本可以直接丢入mod中测试。
# 新增条目以#NEW 开头
# 变更条目以#BEFORE ，#AFTER 和#CHANGE 开头，分别是旧的和新的英文以及需要更变的中文条目。

file_cn = open("old/zh_CN.lang", 'r+', encoding = 'UTF-8')
file_en = open("new/en_US.lang", 'r+', encoding = 'UTF-8')
file_en_old =  open("old/en_US.lang", 'r+', encoding = 'UTF-8')
file_out = open("out_put/en_US.lang", 'w', encoding = 'UTF-8')

en_list = list()

en_dict = dict()
cn_dict = dict()
en_old_dict = dict()

for line in file_en.readlines():
	print('[' + str(len(en_list) + 1) + ']' + 'Loading en_US.lang: ' + line)
	if line != None and line[0] != '#' and '=' in line:
		line_list = line.split('=', 1)
		line_key = line_list[0]
		line_value = line_list[1]
		en_list.append(line_key)
		en_dict[line_key] = line_value
	else:
		en_list.append('#craft love comments' + line)

print('en_US.lang has been loaded!')

for line in file_en_old.readlines():
	if line != None and line[0] != '#' and '=' in line:
		line_list = line.split('=', 1)
		line_key = line_list[0]
		line_value = line_list[1]
		en_old_dict[line_key] = line_value

print('the old version of en_US.lang has been loaded!')

for line in file_cn.readlines():
	print('Loading zh_CN.lang: ' + line)
	if line != None and line[0] != '#' and '=' in line:
		line_list = line.split('=', 1)
		line_key = line_list[0]
		line_value = line_list[1]
		cn_dict[line_key] = line_value

for line in en_list:
	if '#craft love comments' in line:
		print(file_out.writelines(line.replace('#craft love comments', '')))
	else:
		try:
			if en_old_dict[line] != en_dict[line]:
				print(file_out.writelines('#BEFORE ' + line + '=' + en_old_dict[line]))
				print(file_out.writelines('#AFTER ' + line + '=' + en_dict[line]))
				print(file_out.writelines('#CHANGE ' + line + '=' + cn_dict[line]))
			else:
				print(file_out.writelines(line + '=' + cn_dict[line]))
		except:
			print(file_out.writelines('#NEW ' + line + '=' + en_dict[line]))

print('Done!')

file_cn.close()
file_en.close()
file_out.close()
file_en_old.close()
