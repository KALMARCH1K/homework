def f(n):
    result = ''
    for i in range(1,n//2+1):
         for x in range(i+1,n):
            if n%(i+x)==0 and i!=x:
                result+= str(i)+str(x)

    return result
for i in range(3,21):
    print(f'{i} ---- {f(i)}')