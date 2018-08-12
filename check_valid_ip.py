# This script takes a string (no whitespaces) and the type of IP
# If it's either valid ipv4 or ipv6 it returns True
# Else returns false. Does not support short form of ipv6.

class IpAddrValidator:
    def __init__(self, ip_addr: str):
        self.ip_addr = ip_addr
    
    def split_addr_ipv4(self):
        ip_block = self.ip_addr.split('.')
        return ip_block

    def split_addr_ipv6(self):
        ip_block = self.ip_addr.split(':')
        return ip_block

    def check_ipv4(self):
        ip_block = self.split_addr_ipv4()
        if len(ip_block) == 4:
            for ips in ip_block:
                try:
                    if int(ips)/255 > 1 or int(ips)/255 < 0:
                        return False
                except ValueError: ##If contains any character other than numbers
                    return False
            return True
        return False

    # TODO: Handle ipv6 short form.
    def check_ipv6(self):
        valid_chars = 'ABCDEFabcdef0123456789'
        ip_block = self.split_addr_ipv6()
        flag_empty = 0 #Flag if ipaddrs has :: more than once
        if len(ip_block) == 8:
            for ips in ip_block:
                if ips == '': flag_empty += 1
                for ip in ips:
                    if ip not in valid_chars:
                        return False
            if flag_empty > 1: return False
            return True
        return False
