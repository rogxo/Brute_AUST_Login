import json
import re

import requests


def send_get(session, username: str, password: str, company: str):
    url = 'http://10.255.0.19/drcom/login?callback=dr1003&DDDDD=' + username + company + '&upass=' + password + '&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&v='
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
               'Referer': 'http://10.255.0.19/a79.htm'}
    r = session.get(url=url, headers=headers, verify=False)
    s = re.findall(r'\((.*?)\)', r.text)
    j = json.loads(s[0])
    # print(j)
    # print(type(j))
    status = j['result']
    # if status == 1:
    return status


def get_company(session, username: str, password: str):
    companys = ['@aust', '@unicom', '@cmcc', '@jzg']
    for company in companys:
        try:
            ret = send_get(session, username, password, company)
            if ret == 1:
                session.get('http://10.255.0.19/drcom/logout?callback=dr1002&v=')
                return company
        except:
            session.get('http://10.255.0.19/drcom/logout?callback=dr1002&v=')
            return


if __name__ == '__main__':
    print('please call as a module')
