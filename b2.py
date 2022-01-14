# Viết chương trình tính tổng của các chữ số của môt số nguyên n trong Python. 
# Số nguyên dương n được nhập từ bàn phím. Với n = 1234, tổng các chữ số: 1 + 2 + 3 + 4 = 10
# a, Nhập và in ra màn hình tên đệm của mình 
# b, Chạy chương trình bằng cách nhập n bằng độ dài tên của mình và tên đệm ví dụ MANH CUONG thi n = 4 + 5 = 9
na=input("nhập tên đệm của mình:")
print("tên đệm của bạn là:",na);
def totalNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
n = int(input("nhập số nguyên dương n(=độ dài tên của mình và tên đệm)= "));
print("tổng các chữ số của", n , "là", totalNumber(n));
