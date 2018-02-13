def fibonacci():
    fibo = [1, 1]
    prevnum = 1
    num = 1
    while num < 4000000:
        prevnum, num = num, num + prevnum
        fibo.append(num)
    fourmil = 0
    for i in fibo:
        if i % 2 == 0:
            fourmil =+ i
    return fourmil
print(fibonacci())
