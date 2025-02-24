t = int(input("Enter no. of test cases: "))
for _ in range(t):
    n = int(input("Enter no. of boys and girls: "))
    boys = list(map(int, input("Enter heights of boys: ").split()))
    girls = list(map(int, input("Enter heights of girls: ").split()))
    heights = list(zip(boys + girls, [-1]*n + [1]*n))
    heights.sort()
    for i in range(len(heights) - 1):
        if heights[i][1] == heights[i + 1][1]:
            print("NO")
            break
    else:
        print("YES")
