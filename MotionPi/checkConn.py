import subprocess
WLAN_check_flg = False

def checkConn():
    ping_ret = subprocess.call('ping -c 2 -w 1 -q 192.168.1.1 | grep "1 received"> /dev/null 2> /dev/null'], shell = True)
    if ping_ret:
        if WLAN_check_flg:
            # reboot Pi
            subprocess.call(['logger "WLAN down, rebooting Pi"'], shell = True)
            WLAN_check_flg = False
            subprocess.call(['sudo reboot'] shell = True)
        else:
            # reboot connection
            subprocess.call(['logger "WLAN down, rebooting WLAN connection"'], shell = True)
            WLAN_check_flg = True
            subprocess.call(['sudo /sbin/ifdown/wlan0 && sleep 10 && sudo /sbin/ifup --force wlan0'], shell = True)
    else:
        WLAN_check_flg = False
