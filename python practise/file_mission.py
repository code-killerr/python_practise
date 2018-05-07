#将一个对话文本中的对话分为甲乙两部分输出并分段对话
f = open('对话.txt')
jia = []
yi = []
cout = 1
for each_line in f:
    if each_line[:5] != '=====':
        (role,line_spoken) = each_line.split(':',1)#split(sep=None,maxsplit = -1)第一个不带参数默认空格切片字符串，第二个参数如果设置则分隔该数量的字符串返回切片后的拼接列表，切成两片分别给role和line_spoken
        if role == '甲':
            jia.append(line_spoken)
        if role == '乙':
            yi.append(line_spoken)#分辨是谁说的话
    else:
        name_jia = 'jia_' + str(cout) + '.txt'
        name_yi = 'yi_' + str(cout) + '.txt'
        
        jia_file = open(name_jia,'w')
        yi_file = open(name_yi,'w')
        
        jia_file.writelines(jia)
        yi_file.writelines(yi)
        
        jia_file.close()
        yi_file.close()
        
        jia = []
        yi = []
        cout+=1

f.close()