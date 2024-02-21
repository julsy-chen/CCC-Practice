userInput = input()
d = userInput.split()
d = list(map(int, d))

# data process
c = [0]
# there are four numbers
for i in range(0, 4):
    c.append(c[i] + d[i])

# output
for i in range(0, 5):
    r = []
    for j in range(0, 5):
        distance = c[j] - c[i]
        if (distance<0):
            distance *= -1
        r.append(distance)

    print(*r)