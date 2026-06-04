
list = [1,2,3,4,5] #Same iter() work for Dictionary / Map amd range(5)

I = iter(list)
print(I)
print(I.__next__())
print(I)
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(next(I))

I = iter(list)


for i in I:
    print("->",i)