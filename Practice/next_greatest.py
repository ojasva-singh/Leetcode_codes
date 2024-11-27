
n = int(input("Enter the number of elements in the list: "))
arr = list(map(int, input().split()))

k = int(input("Enter the value of k: "))
ng = float('inf')

for i in range(len(arr)):
    if arr[i]>k and arr[i]<ng:
        ng = arr[i]

print(ng)