# LearnB4
EX4
## Bài tập find fair
n = int(input(" Nhập số phần tử trong chuỗi"))
lst = []
lst2 = []
for i in range(n):
    lst.append(int(input("Nhập từng phần tử trong chuỗi không trùng nhau: ")))
lst.sort()
print ("Chuỗi đã được nhập vào là: ",lst)
s = int(input("Nhập tổng sum: "))
for v in range (len(lst)):
    for j in range (v+1,len(lst)):
      if (lst[v]+ lst[j]) == s:
        d = (lst[v],lst[j])
        lst2.append(d);         
print("Danh sách các cặp phần tử có tổng bằng ",s, "là: ", lst2)
## Bài tập Print star
### hình sao 1
n = int(input("Nhập số n: "))
for i in range (0,n+1) :
    for j in range (0,n-i) :
        print (end= "  ")
    for j in range (0, i):
        print ('* ', end="")
    print ("\r")
### hình sao 2
n = int(input("Nhập số n: "))
for i in range (0,n+1) :
    for j in range (0,n-i) :
        print (end= "  ")
    if i == n: i=(n)*2
    for j in range (0, i):
        print ('* ', end="")
    print ("\r")
for i in range (n-1, 0, -1) :
    print(n*2*' ', end='')
    for k in range (0,i):
        print("* ", end='')
    print("\r")

## Bài tập countdown Xmas
import time
from datetime import datetime
a = datetime (2021,12,24,23,59,59,999999)
while True :
  b = datetime.now()
  c=a-b
  print("Countdown to Xmas 2021:" ,c)
  time.sleep(5)

## Bài tập đếm số
from collections import Counter
n = int (input("Nhập số phần tử trong list:"))
my_list=[]
for i in range(n):
    my_list.append(int(input("Nhập từng phần tử trong list: ")))
print("List đã nhập là: ",my_list)
print (Counter(my_list) )
## Bài tập Dictionary Key
my_list = []
my_dict1=dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)
my_dict2= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
for i in my_dict1.values(): 
  if i in my_list: 
    continue 
  else:
    my_list.append(i)
for j in range(0, len(my_dict2)):
  c = list(my_dict2[j].values())
  if c in my_list: 
    continue 
  else:
    my_list.append(c)
print(my_list)