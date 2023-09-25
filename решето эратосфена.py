def eratosthenes(n):
    a = []
    b = []
 
    if n < 4:
        return
 
    for i in range(2, n + 1, 1):
        a.append(i)
 
    while a:
        for i in a[1:]:
            if i % a[0] == 0:
                b.append(i)
                a.remove(i)
        a = a[1:]
 
    for i in b:
        print(i, end=" ")
