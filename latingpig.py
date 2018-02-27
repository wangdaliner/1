import re
print ("现在进行拉丁猪文字游戏")
print ("请您输入一个英文单词")
a = input()
print ("您输入单词是：",a)

c = ["a","i","u","e","o"]
e =len(a)

for i in range(len(c)):
    yn = re.search(c[i],a)
    if yn != None:
        d = re.search(c[i], a).span()
        break

f=(d[1])-1
g = a[f:e]
j = a[0:f]
u = [g,"-",j,"ay"]

p = "".join(u)
print (p)