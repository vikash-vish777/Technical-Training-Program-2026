# i/p= 6 30 50
#      29 38 12 48 39 55

# o/p= 38 48 39


num, start, end = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(num):
    if start <= arr[i] <= end:
        print(arr[i], end=" ")