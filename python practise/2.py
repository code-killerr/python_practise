a="hello"#定义字符串可以为单引号或双引号
b='world'#字符串的赋值
d=6#定义变量并赋值
e=5#使用变量前一定要定义并赋值
print(a+b)#变量名定义只能为数字,字母与下划线
print(d+e)#定义变量名应用下划线代替空格并且第一个字母大写例:Array_Project
a='world'#字符串变量可以被重新初始化
print(a+b)
c=a+b#字符串的拼接
print(c)
s ='let\'s go'#字符串中如若需要单引号或双引号使用转义符
print(s)#字符串中有\时可以使用\\替换
s ="c:\\2"
print(s)
s =r'c:\2'+'\\'#或者使用r''变为原始字符串,但是结尾不能有反斜杠
print(s)
s ="""嘿，你好
嘿，你也好
all right,nice to see you
nice to see you too.
"""#如若储存多行字符串可使用"""
print(s)
