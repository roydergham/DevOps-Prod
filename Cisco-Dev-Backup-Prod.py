import paramiko
import datetime
import sys
import os



# define variables
user = 'cisco_backup'
password = 'UNescwa@##'
#time_now  = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
time_now  = datetime.datetime.now().strftime('%Y_%m_%d')
filepath = "c:\\Users\\Roy\\Documents\\"
devicelist = "ESCWA-SW-List.txt"
port=22



def main():
    if not os.path.isfile(filepath+devicelist):
        print("File path {} does not exist. Exiting...".format(filepath+devicelist))
        sys.exit()
    # open device file
    input_file = open(filepath + devicelist, "r")
    iplist = input_file.readlines()
    input_file.close()
    with open(filepath+devicelist) as file:
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
        outfile = open(filepath + ipaddr + "_" + time_now + ".txt", "w")
        for char in list:
            outfile.write(char)
        ssh.close()
        outfile.close()
    except ssh.connect() as err:
        print(err)


if __name__ == '__main__':
    main()

