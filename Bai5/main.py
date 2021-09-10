from typing import Counter
from collections import Counter

n= int(input(print("Nhập số phần tử trong list: ")))
my_list= []
for i in range (0,n):
    a = int(input(print(" Nhập phần tử thứ " ,i, ': ')))
    my_list.append(a)
my_list.sort()
def mean():
    s = sum(my_list)
    b = s/n
    return b
def median():
    c = n//2
    if n%2 == 0:
        d = ((my_list[c-1])+ (my_list[c]))/2
    else:
        d = my_list[c]
    return d
def mode():
    my_lst2 = []
    my_lst3 = []
    my_lst1 = Counter(my_list)
    for i in my_lst1.values(): 
        my_lst2.append(i)
    e = max(my_lst2)
    for j in my_lst1.keys() :
        if my_lst1[j] == e :
            my_lst3.append(j)
    return (my_lst3,e)
print ("List được nhập vào là: ", my_list)
print (" Các giá trị mean, mdeian, mode của list lần lượt là: ", mean(),', ', median(),', ', mode())

#Bài đếm số
## Ví dụ 1
s = str(input("Nhập chuỗi muốn đếm: "))
def dem_so():
  numbers = sum(c.isdigit() for c in s)
  words   = sum(c.isalpha() for c in s)
  uppers  = sum(c.isupper() for c in s)
  lowers   = sum(c.islower() for c in s)
  result_dict={
        "LETTERS":words,
        "CASE":{"UPPER CASE":uppers, "LOWER CASE":lowers},
        "DIGITS":numbers}
  print("Kết quả là: ",result_dict)  
dem_so()
## Ví dụ 2
s= str(input("Nhập chuỗi muốn đếm: "))
def dem_chuoi():
  number=0
  upcase =0
  lower =0
  for c in s:
    a = ord(c)
    if 48 <= a <= 57:
      number +=1
    elif 65<=a <= 90:
      upcase +=1
    elif 97 <=a <=122:
      lower +=1
  letter = upcase + lower
  result_dict={
        "LETTERS":letter,
        "CASE":{"UPPER CASE":upcase, "LOWER CASE":lower},
        "DIGITS":number
 }   
  print(result_dict)

dem_chuoi()