# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 12:06:17 2018

@author: Administrator
"""
src=['E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170207.xlsx'
      ,'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170208.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170209.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170210.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170211.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170212.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170213.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170511.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170512.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170513.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170514.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170515.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170516.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170517.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170810.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170811.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170812.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170813.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170814.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170815.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20170816.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20171109.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20171110.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20171111.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20171112.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20171113.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20171114.xlsx',
      'E:\\mathlab\\2018年MathorCup数学建模挑战赛D题\\2018年MathorCup数学建模挑战赛D题附件\\附件1\\20171115.xlsx']
import xlrd
path=0
Type_1=0
Type_0=0
Type_null=0
for path in src:
    data=xlrd.open_workbook(path)#打开相应excel文件
    sheet_1_by_index=data.sheet_by_index(0)#取出文件列表
    num=sheet_1_by_index.col_values(3)#读取第四行数据
    n_of_cols=sheet_1_by_index.ncols#具有行数
    i=0
    for i in num:#查找相应数据
        if i == 0.0:
            Type_0+=1
        else:
            if i == 1.0:
                Type_1+=1
            else:
                if i == 'Null':
                    Type_null+=1
print("0:",Type_0)
print("1:",Type_1)
print("null:",Type_null)
