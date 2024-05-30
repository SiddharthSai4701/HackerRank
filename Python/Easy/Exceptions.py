# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    l = list(map(str, input().split()))
    
    try:
        d = int(l[0])//int(l[1])
        print(d)
    except ZeroDivisionError as e:
        print("Error Code: ", e)
    except ValueError as e:
        print("Error Code: ", e)