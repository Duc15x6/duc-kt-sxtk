# Hãy viết chương trình để tạo ra một dictionary chứa (i, i*i), 
# trong đó i là số nguyên từ 1 đến n (bao gồm cả 1 và n), n được nhập từ bàn phím.
# Sau đó in ra dictionary này ra màn hình. 
# Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
# a, Nhập và in ra màn hình tên của mình
# b, Chạy chương trình bằng cách nhập n bằng độ dài tên của mình ví dụ cuong thi n = 5
na=input("nhâp tên của mình vào: ")
n=int(input("nhập số nguyên dương n(=độ dài tên của mình):"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print("tên của bạn là:",na)
print(d)
