import requests
import sys
import subprocess


site = ''

def lines(testo):
    return '\n**************************************************' + '\n--> \033[93m' + testo + '\n\033[0m' + '**************************************************\n'

def check_header():
    response = requests.get(site)
    head = response.headers
    out = ''
    for x in head:
        out += x + ': ' + head[x] + '\n'
    return out.strip()

def check_gobuster():
    wordlist = './dir-wordlist/common.txt'
    subprocess.run(['gobuster', 'dir', '-u', site, '-w', wordlist, '-z'])
    
def check_richieste():
    ric = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'OPTIONS']
    out = ''
    for x in ric:
        result = subprocess.run(['curl', '-X', x, site, '-I', '-s'], stdout=subprocess.PIPE)
        result = result.stdout.split(b'\r\n')[0]
        space = ' ' * (7 - len(x))
        col = '\033[92m'
        if b'40' in result:
            col = '\033[91m'
        out += col + x + '\033[0m' + space + ' --> ' + result.decode() + '\n'
    return out.strip()



if __name__ == '__main__':
    site = sys.argv[1]
    print(lines('Headers'))
    print(check_header())
    print(lines('Richieste disponibili'))
    print(check_richieste())
    print(lines('Gobuster'))
    print(check_gobuster())
    