#該如何讀取xml檔案
import xml.etree.ElementTree as ET
def compound_interest(x,s,y):
    total = 0 #計算複利的總和
    for i in range(y):#總共y年
        total = (total + x)#經過複利的金額+新投資的金額
        total = total*(1+s/100)#複利
    return total
# 解析XML文件
tree = ET.parse("setting.xml")#讀取setting.xml的檔案
root = tree.getroot()#建立樹結構
#如何把樹結構轉化成python可以使用的資料?
# 创建一个空字典:在python裡類似樹結構的東西,都是用{}做建立

data_dict = {}#data = {key : value}
for element in root:
    key = element.tag #讀取:x/s/y
    value = element.text  #讀取裡面得文字 10000 10 20(被tag包夾的文字)
    data_dict[key] = value #把資料存到python裡的字典處理
# 打印字典
print(data_dict)
x = int(data_dict['x'])
s = int(data_dict['s'])
y = int(data_dict['y'])
# x = int(input("每年投資的金額"))
# s = int(input("年利率"))
# y = int(input("年份"))

print(compound_interest(x,s,y))#算出成果
#不但要計算出成果且要存智記事本
#打開記事本檔案
file = open("result.txt","w",encoding="utf-8")
#result.txt -> 檔案名稱
#"w" -> write寫入
#encoding -> 文字編碼 繁體用的是"utdf-8" 簡體"-5"
file.write("本金:"+str(x)+"\n")
file.write("年利率:"+str(s)+"\n")
file.write("投資年分:pip"+str(y)+"\n")
file.write("-----------這是可以得到的總金額-------------\n")
num = compound_interest(x,s,y)
file.write(f"{num:.2f}元")
file.close()