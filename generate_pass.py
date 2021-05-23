f = open('password.txt', mode='a+')
for i in range(int(input()), int(input())):
    f.write('0' + str(i) + '\n')
