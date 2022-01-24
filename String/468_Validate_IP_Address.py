# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 18:02:30 2022

@author: Fan Luo
"""
"""
468. Validate IP Address

Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, 
"IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. 
For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", 
    while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') 
    and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses,
 while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
 
Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
"""
class Solution(object):
    def validIPAddress(self, queryIP):
        def ipv4(queryIP):
            ip = queryIP.split(".")
            
            for c in ip:
                if len(c) == 0 or len(c) > 3:
                    return "Neither"

                if (c[0] == '0' and len(c) != 1) or int(c) > 255 or (not c.isdigit()):
                    return "Neither"
                
            return "IPv4"
                    
            
            
        def ipv6(queryIP):
            ip = queryIP.split(":")
            
            for c in ip:
                if len(c) < 1 or len(c) > 4:
                    return "Neither"
                for i in c:
                    if i not in "abcdef0123456789":
                        return "Neither"
            return "IPv6"
        
        if len(queryIP.split(".")) == 4:
            return ipv4(queryIP)
        
        if len(queryIP.split(":")) == 8:
            return ipv6(queryIP)
        
        return "Neither"
    
if __name__ == '__main__':
    queryIP = "172.16.254.1"
    print(Solution().validIPAddress(queryIP))       