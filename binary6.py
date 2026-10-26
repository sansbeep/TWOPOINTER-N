def isPairSum(A, N, X):

    for i in range(N):
        for j in range(N):

            if(i == j):
                continue

            if (A[i] + A[j] == X):
                return [A[i], A[j]]

            if (A[i] + A[j] > X):
                break

    return 0


arr = [2, 3, 5, 8, 9, 10, 11, 13, 16, 17, 18, 20, 25]


val = 37

print("Pair with the sum equal to {} is - {}".format(val, isPairSum(arr, len(arr), val)))