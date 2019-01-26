def quick_sort(list):

    quick_sort_helper(list, 0, len(list)-1)


def quick_sort_helper(list, first, last):

    if first < last:
        split_point = partition(list, first, last)
        quick_sort_helper(list, first, split_point-1)
        quick_sort_helper(list, split_point+1, last)

def partition(list, first, last):

    pivot = list[first]
    left = first+1
    right = last
    done = False

    while not done:
        while left <= right and list[left] <= pivot:
            left += 1

        while list[right] >= pivot and right >= left:
            right -= 1

        if left > right:
            done = True

        else:
            temp = list[left]
            list[left] = list[right]
            list[right] = temp

    temp = list[first]
    list[first] = list[right]
    list[right] = temp

    return right

# https://www.youtube.com/watch?v=COk73cpQbFQ&t=0s&index=8&list
# =PL2_aWCzGMAwKedT2KfDMB9YA5DgASZb3U


test = [54,26,932,17,9,31,44,55,20,25,27,29,90,90.5]

quick_sort(test)
print(test)