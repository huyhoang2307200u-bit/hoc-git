def kiemtra(n):
    if n > 6 and n % 3 == 0:
        return True
    return False
if __name__ == "__main__":
    n = int(input("Nhap so nguyen: "))
    if kiemtra(n):
        print(f"{n} tong 3 so tu nhien lien tiep")
    else:
        print(f"{n} khong phai tong 3 so tu nhien lien tiep")