import paramiko
import datetime
import sys
import os

# define variables
user = 'cisco_backup'
password = 'UNescwa@##'
time_now  = datetime.datetime.now().strftime('%Y_%m_%d')
parent_directory = "c:\\Users\\Roy\\Documents\\"
backup_directory = parent_directory + time_now + "\\"
devicelist = "SW-List.txt"
port=22
dir = os.path.join(parent_directory, backup_directory)
if not os.path.exists(dir):
       os.mkdir(dir)

def main():
    if not os.path.isfile(parent_directory+devicelist):
        print("File path {} does not exist. Exiting...".format(parent_directory+devicelist))
        sys.exit()
    # open device file
    input_file = open(parent_directory + devicelist, "r")
    iplist = input_file.readlines()
    input_file.close()
    with open(parent_directory + devicelist) as file:
        for ipaddr in file:
            ipaddr = ipaddr.strip()
            sw_backup(ipaddr)

def sw_backup(ipaddr):
    # loop through device list and execute commands
    print(ipaddr)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ipaddr, port, user, password, look_for_keys=False)
        stdin, stdout, stderr = ssh.exec_command('show run')
        list = stdout.readlines()
        outfile = open(backup_directory + ipaddr + "_" + time_now + ".txt", "w")

        for char in list:
            outfile.write(char)
        ssh.close()
        outfile.close()
    except ssh.connect() as err:
        print(err)


if __name__ == '__main__':
    main()

