import requests
import hashlib
import random 
import time

def hex5(action,tim,randstr):
    manipulator = hashlib.md5()
    manipulator.update((action+tim+randstr).encode())
    return manipulator.hexdigest()

headers = {
    'Referer': 'http://www.porters.vip/verify/sign/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

if __name__ == "__main__":    
    action = ''.join([str(random.randint(0,9)) for _ in range(5)])
    tim = str(round(time.time()))
    randstr = ''.join(random.sample([chr(_) for _ in range(65,91)],5))
    hexs = hex5(action,tim,randstr)
    args = '?actions=' + action + '&tim=' + tim + '&randstr=' + randstr + '&sign=' + hexs
    r = requests.get('http://www.porters.vip/verify/sign/fet'+args,headers=headers)
    print(r.status_code)
    print(r.text)