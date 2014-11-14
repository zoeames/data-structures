def bubbleSort(stuff):
    if isinstance(stuff, str):
        stuff = list(stuff)
    for stuffIndex in range(len(stuff)-1, 0, -1):
        for i in range(stuffIndex):
            if stuff[i]>stuff[i+1]:
                stuff[i], stuff[i+1] = stuff[i+1], stuff[i]
    print(stuff)

nums = [8, 3, 21, 9, 3, 5, 12, 4, 17]
bubbleSort(nums)

letters =['n', 'a', 's', 'h', 'v', 'i', 'l', 'l', 'e']
bubbleSort(letters)


word = 'nashville'
bubbleSort(word)


def quickSort(stuff):
    less = []
    more = []
    pvt = []
    if len(stuff) > 1:
        pivot = stuff[0]
        for i in stuff:
            if i < pivot:
                less.append(i)
            if i == pivot:
                pvt.append(i)
            if i > pivot:
                more.append(i)
        return quickSort(less) + pvt + quickSort(more)
    else:
        return stuff


print('Quick Sort:')
nums2 = [8, 3, 4, 17, 1]
nums2 = quickSort(nums2)
print(nums2)