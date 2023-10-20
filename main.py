#該如何讀取xml檔案
import xml.etree.ElementTree as ET
def compound_interest(x,s,y):
    total = 0 #計算複利的總和
    for i in range(y):#總共y年
        total = (total + x)#經過複利的金額+新投資的金額
        total = total*(1+s/100)#複利
    return total
# 解析XML文件
tree = ET.parse("setting.xml")
root = tree.getroot()
# 创建一个空字典
data_dict = {}
# 遍历XML元素并将其存储在字典中
for element in root:
    key = element.tag  # 元素的标签作为字典的键
    value = element.text  # 元素的文本内容作为字典的值
    data_dict[key] = value
# 打印字典
print(data_dict)
x = int(data_dict['x'])
s = int(data_dict['s'])
y = int(data_dict['y'])
# x = int(input("每年投資的金額"))
# s = int(input("年利率"))
# y = int(input("年份"))

print(compound_interest(x,s,y))