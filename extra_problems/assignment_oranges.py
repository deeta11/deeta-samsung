n = int(input("Enter n number of oranges plucked: "))
d = list(map(int, input("Enter the diameters of the oranges respectively: ").split()))
key = d[n - 1]

for i in range(n-1):
    for j in range(i + 1, n):
        if d[i] > d[j]:
            d[i], d[j] = d[j], d[i]

low,high = 0, n-1
mid = -1
while low <= high:
    mid = (low + high) // 2
    if d[mid] == key:
        break
    elif key < d[mid]:
        high = mid - 1
    else:
        low = mid + 1

if mid != -1:
    print(d)
    print(f"{d[:mid]} will go to the children")
    print(f"{d[mid+1:]} will go to the market")

