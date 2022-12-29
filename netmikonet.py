from netmiko import ConnectHandler
# import time
# time.sleep(1)
CSR = {
    "device_type": "cisco_ios",  #device type is defined by netmiko
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    #"ip":"sandbox-iosxe-recomm-1.cisco.com",
    #"port":22,    #for ssh-portno is 22,for netconf - 830
    "username": "developer",
    "password": "C1sco12345"
}

net_connect=ConnectHandler(**CSR)
# output_runhost=net_connect.send_command('show run | i host')
output=net_connect.send_command('show ip int brie')
# print(output)
output_clock=net_connect.send_command('show clock')
# print(output_clock)
output_routes=net_connect.send_command('show ip ro')
# print(output_routes)

output_runconfig=net_connect.send_command('show run')
print(output_runconfig)
# print(output_runhost)
net_connect.disconnect()