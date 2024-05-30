n = int(input())
phone_book = {}
for i in range(n):
    deets = input().split()
    phone_book[deets[0]] = deets[1]
    
while True:
    try:
        name = input()
        if name in phone_book:
            print(name + '=' + phone_book[name])
        else:
            print("Not found")
    except EOFError:
        break