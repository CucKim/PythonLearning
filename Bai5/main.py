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
        d = ((my_list[c-1])+ (my_list[c+1]))/2
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