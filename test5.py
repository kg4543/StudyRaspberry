def three(sum):
    for i in range(100):
        if i % 3 == 0 :
            sum += i
    return sum

def seven(sum):
    for i in range(100):
        if i % 7 == 0 :
            sum += i
    return sum

if __name__ == '__main__' :
    i = 0
    a = three(i)
    b = seven(i)
    print('3의 배수 합: {0} \n 7의 배수 합: {1}'.format(a, b))