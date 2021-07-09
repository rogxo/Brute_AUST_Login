f = open('password.txt', mode='a+')
a=input()
flag=int(a[0])
print(flag)
b=input()

if flag==0:
    for i in range(int(a),int(b)):
        f.write('0' + str(i) + '\n')

if flag:
    for i in range(int(a),int(b)):
        f.write(str(i) + '\n')
