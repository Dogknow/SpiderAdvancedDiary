# -*- encoding: utf-8 -*-
#Time : 2020/04/09 11:41:16

# salt: 15864007000413 #ts加一位0-9
# sign: dd68241f9728c52928b8b79701b8f66a md5("fanyideskweb" + e + salt + "Nw(nmmbP%A-r6U3EUn]Aj") e是要查询的字符串
# ts: 1586400700041 #13位时间戳
# bv: 70244e0061db49a9ee62d341c5fed82a md5(ua的一部分)

import hashlib
import time
import requests
from random import randint

headers = {
    # 'Cookie': '_ntes_nnid=86b7ecdaae6bf1d0eb845c962bb4ed29,1583757711258; OUTFOX_SEARCH_USER_ID_NCOO=575308741.0422249; OUTFOX_SEARCH_USER_ID="1977270650@10.108.160.17"; JSESSIONID=aaaN0U3pTlCaIcRcw2Cfx; ___rl__test__cookies=1586402971425',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

def get_cookies():
    cookie_list = []
    r = requests.get('http://fanyi.youdao.com/')
    for c in r.cookies:
        cookie_list.append('%s=%s'%(c.name,c.value))
    cookies = ';'.join(cookie_list)
    return cookies

def mmd5(s):
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()

def get_data(word):
    ts = str(time.time()*1000)
    salt = ts + str(randint(0,9))
    sign = mmd5('fanyideskweb'+word+salt+'Nw(nmmbP%A-r6U3EUn]Aj')
    bv = mmd5('5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')
    data = {
    'i': word,                                                
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': 2.1,
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
    'ts':ts,
    'salt':salt,
    'sign':sign,
    'bv':bv,
    }
    return data


if __name__ == "__main__":
    cookies = get_cookies() 
    headers.update(Cookie=cookies)
    while True:
        word = input('给爷输:')
        data = get_data(word)
        r = requests.post(url,data=data,headers=headers)
        print(r.text)