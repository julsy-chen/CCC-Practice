num = int(input())

l1 = input()
l1 = l1.split()
l1 = list(map(int, l1))

l2 = input()
l2 = l2.split()
l2 = list(map(int, l2))

b1 = False
b2 = False
c = 0

for i in range(0, num):
    if l1[i] == 1:
        if b1 == True:
            c += 1
        else:
            c += 3
            b1 = True
    else:
        b1 = False
    
    # checking next line
    if l2[i] == 1:
        if b1 == True:
            if b2 == True:
                if i % 2 == 0:
                    c -= 1
                else:
                    c += 1
            else: # b2 is false
                if (i + 1) % 2 == 0:
                    c += 3
                else:
                    c += 1
        # b1 was false
        else:
            if b2 == True: 
                c += 1
            else: # b2 is false
                c += 3
        b2 = True
    else:
        b2 = False
            
print(c)
