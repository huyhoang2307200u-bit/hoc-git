a,b,c = map(int,input().split())
if a < 0 and b < 0 and c < 0:
    print("Negative")
elif a > 0 and b > 0 and c > 0: 
    if a == b and b == c:
        print("la tam giac deu")
    elif a == b or b == c or a == c:
        print("la tam giac can")
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("la tam giac vuong")
    elif a + b > c and a + c > b and b + c > a:
        print("la tam giac thuong")
    else:
        print("khong phai la tam giac")