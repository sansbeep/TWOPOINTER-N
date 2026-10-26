MAX_VAL = 100000000

def printClosest(arr, n, x):

    res_l, res_r = 0, 0

    l, r, diff = 0, n-1, MAX_VAL
    while r > l:
        if abs(arr[l] + arr[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l] + arr[r] - x)

        if arr[l] + arr[r] > x:
            r -= 1
        else:
            l += 1

    print('The closest pair to sum {} is {} and {}'.format(x, arr[res_l], arr[res_r]))

if __name__ == "__main__":
    arr = [10, 22, 24, 28, 29, 30, 40, 47, 50, 67, 70, 75, 80, 82, 85, 87, 89, 90, 94, 96, 98]
    n = len(arr)
    x=68
    printClosest(arr, n, x)