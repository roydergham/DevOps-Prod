
#!/usr/bin/env python
import requests  ## pip install requests
import sys
import os
import socket
from colorama import Fore

filepath = 'WebsiteList.txt'


def main():
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath) as file:
        for line in file:
            line = line.strip()
            site_up(line)

def site_up(website):
    """ function to monitor up time """
    try:
        r = requests.get(website.format(socket.gethostbyname(socket.gethostname())))
        rs = requests.get(website.format(socket.gethostbyname(socket.gethostname())))
        if r.status_code == 200 or rs.status_code == 200:
            print(Fore.BLUE+website, Fore.RESET+'Site ok')
        else:
            print(Fore.BLUE+website, Fore.RED+'Site Currently down', Fore.RESET)
    except requests.ConnectionError as err:
        print(Fore.BLUE+website, Fore.RED+'Site Currently Down or Experiencing Some Error', Fore.RESET)
        print(err)

if __name__ == '__main__':
    main()

