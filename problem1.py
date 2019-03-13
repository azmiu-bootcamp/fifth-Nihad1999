a = int(input("1-ci ededi daxil edin-> "))
b = int(input("2-ci ededi daxil edin-> "))
c = int(input("3-ci ededi daxil edin-> "))


s = 0

if a==b and a==c:
    s = 3
elif a==b or a==c or b==c:
    s=2


print(s)
