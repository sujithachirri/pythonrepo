from netmiko import ConnectHandler
CSR = {
    "device_type": "cisco_ios",  #device type is defined by netmiko
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345"
}
net_connect=ConnectHandler(**CSR)
hostname = net_connect.send_command('show run | i host')
hostname.split(" ")
hostname,device,*rest=hostname.split(" ")
print("backing up " + device)

filename="C:/Users/user738/PycharmProjects/pythonProject1/sujitha1.txt"

showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver=net_connect.send_command('show var')
log_file=open(filename,"a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")

net_connect.disconnect()