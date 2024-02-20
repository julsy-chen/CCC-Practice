num = int(input())
yesterday = list(input())
today = list(input())
counter = 0

for i in range(0, num):
    if yesterday[i] == "C":
        if today[i] == "C":
            counter += 1

print(counter)