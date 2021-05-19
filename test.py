def factorial(num):
    if num < 0:
        return
    if num == 0:
        return 1
    value = 1
    for i in range(1, num + 1):
        value *= i
    return value


def print_num():
    factorial_dic = {}
    for i in range(10):
        factorial_dic[i] = factorial(i)
    print(list(str(10)))
    for i in range(3628800):
        li = list(str(i))
        sum_ = 0
        for b in li:
            sum_ += factorial_dic[int(b)]
        if sum_ == i:
            print(i)


if __name__ == '__main__':
    print_num()
