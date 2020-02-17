#正则表达式使用re库
#正则表达式有独特的语法以及一个独立的处理引擎
#"."代表匹配任意字符，
import re  
data = 'abcde' 
reg = 'a...e'   #代表匹配其中5个字符长度且开头为a结尾为e的字符串
out = re.findall(reg,data)  #调用正则表达式中的查找函数
print(out)
#"*"代表匹配0或多次前面出现的字符。所以当前面放.代表匹配多次.如果没有点代表前面匹配0
reg = 'a.*e'#代表匹配其中以a开头e结尾的字符串
out = re.findall(reg,data)
print(out)#输出abcde表示匹配a.(任意个.)e
reg = 'a*e'
out = re.findall(reg,data)
print(out)#输出e表示匹配a(任意个a，a可以为0)e
#"+"与"*"的功能相同，区别在于"*"可以匹配到0次，也就是说匹配的字符可以不出现，而"+"匹配的字符最少要出现一次。
reg = 'a+e'
out = re.findall(reg,data)
print(out)#输出空因为匹配ae时a至少要出现一次
#"^"和"$"分别代表匹配字符串起始部分和匹配字符串终止部分。
reg = '^a.*'#表示匹配以a开头的字符串，不加.*表示只匹配字符串开头，加.*表示匹配以a开头的全部字符串
out = re.findall(reg,data)
print(out)
reg = '^b.*'
out = re.findall(reg,data) 
print(out)#如果开头和提供字符串开头不符,不会输出
reg = '.*e$'#和^同理
out = re.findall(reg,data) 
print(out)
#匹配时"?"表示其之前的字符出现0次或1次。
'''\w 匹配字母或数字或下划线或汉字 等价于 '[^A-Za-z0-9_]'。
\s 匹配任意的空白符
\d 匹配数字
\b 匹配单词的开始或结束
'''
reg = '4-?\w{8}'#代表且\d{8}表示匹配\前出现的字符后8位字符？代表出现或者不出现，出现即匹配，不出现则没有作用
data = {'23214-34563432','123124--3342132','4asda1321321sd33412'}
for i in data:
    out = re.findall(reg,i)
    print(out)#表示匹配4后有-或者没有-的8位字符，但是-不能出现两次
#'?'表示非贪心模式只要匹配到一个符合要求的字符就停止
data = 'qqqqqqqaabbaccc'  
reg = 'q+'  
reg1 = 'q+?'  
reg2 = '^q+?'
out = re.findall(reg,data)  
out1 = re.findall(reg1,data)
out2 = re.findall(reg2,data)  
print(out)
print(out1)#遇到一个即停止，生成一个字符串然后继续匹配，如果只需要匹配一次前面加上^即可
print(out2)