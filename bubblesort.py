def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

a = [50,28,98,52,95,10,7,0,26]

print(bubblesort(a))