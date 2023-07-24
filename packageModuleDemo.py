def isPrime(num):
    flag = True
    for i in range(2,num):
        if num % i == 0:
            flag = False
            break
        else:
            continue
    if flag:
        return True
    return False