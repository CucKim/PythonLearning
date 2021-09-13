#Bài tập đảo chuỗi
s = str(input("Nhập chuỗi muốn quy đổi:"))
s1 = s.swapcase()
s2= list (reversed(s1))
s2 = ''.join(s2)
print ("Chuỗi nhập vào ban đầu: " ,s)
print("Chuỗi sau khi quy đổi: ",s2)

#Sắp xếp điểm thi
n = int(input("Khai báo số học sinh trong lớp: "))
diem = []
a = ()
for i in range(1,n+1):
    print("Học sinh số: ",i)
    m1 = int(input("Nhập điểm thi kỳ 1 của học sinh là:"))
    m2 = int(input("Nhập điểm thi kỳ 2 của học sinh là:"))
    e = int(input("Nhập điểm thi cuối kỳ của học sinh là:"))
    a = (m1,m2,e)
    diem.append(a)
print("Danh sách điểm các kỳ của từng học sinh là: ", diem)
print("Danh sách điểm thi sau khi đã sắp xếp là: ", sorted(diem, key=lambda x: x[::-1]))