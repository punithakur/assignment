#input type must be--->2020/9/7:4

import calendar

d={}
def find(keys,value):
    year,month,day = (int(i) for i in keys.split('/'))
    daynum = calendar.weekday(year,month,day)
    days=['Monday','Tuesday','wednesday','Thursday','Friday','Saturday', 'Sunday']
    d[days[daynum]] = daynum+value
    

dic={}
n = int(input("Enter the limit: "))
for i in range(n):
    a,b=input().split(":")
    dic[a]=int(b)


for key , value in dic.items():
    find(key,value)

print(d) 
    

