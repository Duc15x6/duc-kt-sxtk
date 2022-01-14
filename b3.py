# Viết chương trình kiểm tra một số n là số thuận nghịch trong Python. 
# Số nguyên dương n được nhập từ bàn phím.
# a, Nhập và in ra màn hình tên đầy đủ của mình 
# b, chạy chương trình bằng cách nhập n từ bàn phím bằng cách tạo n như sau lấy số lượng họ , tên đệm, tên 
# ví dụ  DINH MANH CUONG thi n = 445 
na=input("nhập tên đầy đủ của mình: ")
def checkThuanNghich(n):
    str1 = str(n);     # ep kieu so n thanh chuoi
    str2 = str1[::-1]; # dao nguoc chuoi str1
    if (str1 == str2):
        return True;
    else:
        return False;
n = int(input("nhập số nguyên dương n (lấy số lượng họ,tên đệm,tên) = "));
print("tên đầy đủ của bạn là:",na);
print("tổng các chữ số của", n , "là", checkThuanNghich(n));