# # Enter your code here. Read input from STDIN. Print output to STDOUT
# n = int(input())
# nums = list(map(int, input().split()))

# nums.sort()

# for i in nums:
#     if nums.count(i) != n:
#         print(i)

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nums = list(map(int, input().split()))
d = {}

for index, element in enumerate(nums):
    if element not in d:
        d[element] = 1
    else:
        d[element]+=1
for key in d:
    if int(d[key]) != n:
        print(key)
        break