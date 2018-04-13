str1="hello world"#可以用c语言字符串数组理解，也可以近似看为元组
print(str1[:5])#输出字符串前5个
print(str1[0])#字符串第0个元素
str1 = str1[:5]+" hi"+str1[5:]#和元组插入方式一样
print(str1)
print(str1.capitalize())#返回首字母大写
print(str1)#不改变原有字符串
str2 = "HELLO PYTHON"
print(str2.casefold())#讲字符串返回为全是小写
print(str2.center(20))#居中字符串20为字符串所占长度默认空格填充，ljust为左对齐并用空格填充
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
print(str3.islower(),str2.islower())#判断是否存在能够大小写的字符，并且是小写
str5="    "
print(str2.isspace(),str5.isspace())#判断字符串是否全为空格
str5="Hello World"
str6="hello world"
print(str5.istitle(),str6.istitle())#判断字符串单词每个开头是否大写
print(str2.isupper(),str3.isupper())#同islower不给过检测是否全部大写
print(str6.join("123"))#在字符串的收尾加上括号中字符串，并重复字符串，直到括号中字符串结束
print(str2.lower())#将字符串中所有大写改为小写
str5="   213  213"
print(str5.lstrip())#去掉字符串左边所有空格
print(str6.partition('lo'))#将字符串以括号中的字符分隔开输出列表
print(str6.split())#以空格为默认参数切片输出列表,括号中数字为多少切多少片
print(str6.replace('world','python'))#将第一个字符串替换成第二个字符串，如若后面有参数表示替换不超过多少次
print(str6.startswith('he'),str6.startswith('HE'))#检测字符串是否为括号中字符开头，可指定范围
print(str5.strip())#默认删除字符串中前面和后面的空格，增加参数可定制删除字符
str6='ASDSDAwewesd'
print(str6.swapcase())#翻转大小写
print(str6.translate(str.maketrans('A','B')))#将A转换为B
print(str6.upper())#将字符串中所有小写字符转换为大写



      
