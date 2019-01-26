test1 = [1, 9, 8, 4, 2, 5, 7, 4, 6, 4, 0]



def merge(L_arr, R_arr, out):
    l = r = i = 0

    while l < len(L_arr) and r < len(R_arr):
        if L_arr[l] <= R_arr[r]:
            out[i] = L_arr[l]
            l += 1
        else:
            out[i] = R_arr[r]
            r += 1
        i += 1

    while l < len(L_arr):
        out[i] = L_arr[l]
        l += 1
        i += 1
    while r < len(R_arr):
        out[i] = R_arr[r]
        r += 1
        i += 1

    return out


a = [1,2,4,6]
b = [3,5,7,8]
c = [1,1,1,1,1,1,1,1]
print(merge(a,b,c))
