# from getmac import get_mac_address as gma
# print(gma())

# import uuid  #uuid--random objects:: 128 bits[random objects/MAC addresses]
# print(hex(uuid.getnode()))

import uuid
print(" the MAC address in formatted way is : ",end="")  #concatinating next line
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)for ele in range (0,8*6,8)][::-1]))  #ele=datacontainer #[::-1]-negative indexing

