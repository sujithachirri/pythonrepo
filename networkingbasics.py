import os , ipaddress

os.system('cls')
while True:
    ip=input('enter ip address')
    try:
        print(ipaddress.ip_address(ip))
        print('ip valid')
    except:
        print('-' *50)
        print('ip not valid' )
    finally:
        if ip =="mango":
            print('script finished')
            break