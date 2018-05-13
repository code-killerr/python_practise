import pickle#翻译为泡菜
list = [2,3,4,5,'hello python']
pk_file = open('pk1_file.pkl','wb')#需要使用二进制写入模式
pickle.dump(list,pk_file)#将第一个参数内容写入第二个文件中
pk_file.close()
pk_file = open('pk1_file.pkl','rb')
list2 = pickle.load(pk_file)
print(list2)