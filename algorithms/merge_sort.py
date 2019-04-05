# Time: O(nlgn)
# Space: O(n)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L_arr = arr[:mid]
        R_arr = arr[mid:]

        merge_sort(L_arr)
        merge_sort(R_arr)
        merge(L_arr, R_arr, arr)
    return arr


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

test1 = [1, 9, 8, 3, 2, 8, 8, 4, 6, 4, 0]

a = [1,2,4,6]
b = [3,5,7,8]
c = [1,1,1,1,1,1,1,1]
# print(merge(a,b,c))

print(merge_sort(test1))
