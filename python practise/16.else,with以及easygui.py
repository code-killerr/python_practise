try:
    int('a')
except ValueError as reason:
    print('wrong:'+str(reason))
else:
    print('无异常')
#ecept可以和except搭配，表示如果未出现异常执行操作
try:
    with open('aaaaaaaa.txt') as f:#with可以自动在文件调用完成后自动关闭
        for each_line in f:
            print(each_line)#注意在with缩进下，表示如若with下内容执行完，with视为文件使用完毕，关闭文件
except OSError as reason:
    print('出错:'+str(reason))
#finally:
 #   f.close()#此处如若文件不存在关闭会出错
#easygui翻译文档http://bbs.fishc.com/thread-46069-1-1.html
#啥玩意，不用这东西玩了，安装全是冲突，和几乎所有处理excl表的插件都冲突，虽然用起来很方便，还是用pyqt5吧
 #为了装这个删了好多插件了还是冲突，删不下去了，不玩了靠
