m =[1,5,2,4,6,7]


uzunluq=len(m)

ustegel = uzunluq + 1
print(ustegel)

data=[]

for i in range(0,uzunluq,2):
    for s in range(1, uzunluq, 2):
        if m[i]< m[s]:
            data.append(m[s])







print(data)
