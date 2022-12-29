#!/usr/bin/env python
import requests  ## pip install requests
import sys
import os
import socket
from colorama import Fore
import datetime

parent_directory = "c:\\Users\\Roy\\Documents\\"
sitelist = 'websiteList.txt'
results = 'website_result.txt'
time_now = datetime.datetime.now().strftime('%Y_%m_%d-%H:%M')
UserComment = input("Enter the test condition")

def main():
    if not os.path.isfile(parent_directory + sitelist):
        print("File path {} does not exist. Exiting...".format(sitelist))
        sys.exit()
    with open(parent_directory + results, "a") as f:
        f.write('----------------------------------------------------------' + '\n''\n'+'\n' +'\n' + '\n')
        f.write(UserComment + '\n')
        f.write('----------------------------------------------------------' + '\n')

    with open(parent_directory + sitelist) as file:
        for line in file:
            line = ('http://' + line.strip())
            site_up(line)

def site_up(website):
    """ function to monitor up time """
    try:
        r = requests.get(website.format(socket.gethostbyname(socket.gethostname())))
        rs = requests.get(website.format(socket.gethostbyname(socket.gethostname())))
        if r.status_code == 200 or rs.status_code == 200:
            print(Fore.BLUE+website, Fore.RESET+'Site ok')
            with open(parent_directory + results, "a") as f:
                f.write(time_now + '\t' + website + '\t' + '\t' +  'Site ok' + '\n')
        else:
            print(Fore.BLUE+website, Fore.RED+'Site Currently down', Fore.RESET)
            with open(parent_directory + results, "a") as f:
                f.write(time_now +  '\t' + website + '\t' + '\t' + 'Site Currently down' + '\n')
    except requests.ConnectionError as err:
        print(Fore.BLUE+website, Fore.RED+'Site Currently Down or Experiencing Some Error', Fore.RESET)
        print(str(err))
        with open(parent_directory + results, "a") as f:
            f.write(time_now +  '\t' + website + '\t' + '\t' + 'Site experiencing some other error' + '\n')


if __name__ == '__main__':
    main()

