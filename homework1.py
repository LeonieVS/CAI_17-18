def fibonacci():
    prevnum = 1
    num = 1
    addition = 0
    while num <= 4000000:
        prevnum, num = num, num + prevnum
        if num % 2 == 0:
            addition += num
    return addition
print(fibonacci())
