import os
import requests

# configuration
HOST = '@'
DOMAIN = os.environ['DOMAIN']
PW = os.environ['NAMECHEAP_DDNS_PW']
ENDPOINT = 'https://dynamicdns.park-your-domain.com/update?'


def get_ip():
    return requests.get('https://dynamicdns.park-your-domain.com/getip').text


def main():
    payload = {'host': HOST, 'domain': DOMAIN, 'password': PW, 'ip': get_ip()}
    r = requests.get(ENDPOINT, params=payload)
    print(r.url)
    print(r.status_code)


if __name__ == '__main__':
    main()
