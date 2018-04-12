str1="hello world"#可以用c语言字符串数组理解，也可以近似看为元组
print(str1[:5])#输出字符串前5个
print(str1[0])#字符串第0个元素
str1 = str1[:5]+" hi"+str1[5:]#和元组插入方式一样
print(str1)
print(str1.capitalize())#返回首字母大写
print(str1)#不改变原有字符串
str2 = "HELLO PYTHON"
print(str2.casefold())#讲字符串返回为全是小写
print(str2.center(20))#居中字符串20为字符串所占长度默认空格填充
print(str1.count('l'))#查找该字符串进行搜索出现次数count(sub[,start[,end]])可规定在特定字段查找
str3="你好世界"
print(str3.encode('utf-8','strict'))#以utf-8进行编码
print(str1.endswith('ld'))#检测是否以某字符串或字符结束
str1="hello\tworld\t"
print(str1.expandtabs(1))#将\t转换为指定空格数
print(str1.find('el',5,8))#寻找字符，可指定范围，没有返回-1有返回1，index和find相似只是没有找到会抛出异常
str3="helloworld123"
print(str1.isalnum(),str3.isalnum())#判断字符串是不是全由字母或数字组成
print(str3.isalpha())#判断字符串是否只有字母
str4="213123"
print(str4.isdigit())#判断字符串是否只包含数字

      
