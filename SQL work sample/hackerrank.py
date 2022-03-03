def miniMaxSum(arr):
    # Write your code here
    max = - math.inf
    min = math.inf
    sum_arr = sum(arr)
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    print(sum_arr - max, sum_arr - min)


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return