import os
import requests

# configuration, set DOMAIN and NAMECHEAP_DDNS_PW as env vars
HOST = '@'
DOMAIN = os.environ['DOMAIN']
PW = os.environ['NAMECHEAP_DDNS_PW']
ENDPOINT = 'https://dynamicdns.park-your-domain.com/update?'


# get the IP address of the system
def get_ip():
    return requests.get('https://dynamicdns.park-your-domain.com/getip').text


# update Namecheap with your current IP address
def main():
    payload = {'host': HOST, 'domain': DOMAIN, 'password': PW, 'ip': get_ip()}
    r = requests.get(ENDPOINT, params=payload)
    print(r.url)
    print(r.status_code)


if __name__ == '__main__':
    main()
