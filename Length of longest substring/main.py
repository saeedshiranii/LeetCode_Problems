string = input("enter a sting: ").lower()
check = []
biggest = []

for i in string[:len(string):]:
    if i in check:
        biggest.append(len(check))
        continue

    else:
        check.append(i)
        for j in string[i:len(string):]:
            if j not in check:
                check.append(j)
            elif j in check:
                biggest.append(len(check))
                check.clear()
                break

print(max(biggest))
