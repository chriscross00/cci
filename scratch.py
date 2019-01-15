def bs(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j + 1] = list[j + 1],list[j]

    return list

a = [87,42,32,52,90,22,74,25,90]
print(bs(a))


def variable(a, *mytuple):
    print(a)
    for var in mytuple:
        print(var)

    return

variable(10, 20, 50, 90)