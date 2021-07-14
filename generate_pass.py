f = open('password.txt', mode='a+')

gender = input("Gender(M/F):")

a = input()
flag = int(a[0])
print(flag)
b = input()

if flag == 0:
    if gender == 'M':
        for i in range(int(a), int(b)):
            if (i % 2) != 0:
                f.write('0' + str(i) + '\n')
    if gender == 'F':
        for i in range(int(a), int(b)):
            if (i % 2) == 0:
                f.write('0' + str(i) + '\n')
if flag:
    if gender == 'M':
        for i in range(int(a), int(b)):
            if (i % 2) != 0:
                f.write(str(i) + '\n')
    if gender == 'F':
        for i in range(int(a), int(b)):
            if (i % 2) == 0:
                f.write(str(i) + '\n')
f.close()
