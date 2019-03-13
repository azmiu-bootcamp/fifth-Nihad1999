def lone_sum(a , b , c):
    if a != b and a != c and b != c:
        print(a+b+c)
    elif a == b and a == c:
        print(0)
    elif a == b and a != c:
        print(c)
    elif a == c and a != b:
        print(b)
    elif b == c and b != a:
        print(a)




a = int(input("a-ni daxil edin-> "))
b = int(input("b-ni daxil edin-> "))
c = int(input("c-ni daxil edin-> "))


lone_sum(a,b,c)
