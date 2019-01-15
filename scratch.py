def bs(list):
    for high in range(len(list)-1, 0, -1):
        for i in range(high):
            if list[i]>list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

    return list



a = [2,8,9,2,8,5,2,85,0,9,1,4]

print(bs(a))