'''
    Runtime: 
        time: iteration takes O(n), n is the length of IP
        space: split IP and reconstruct it takes O(n), n is the length of IP
    Analysis:
        Given: a str representing IP
        Ask: validate if it's a valid IPv4 or IPv6 or neither
'''
class Solution:
    def validIPAddress(self, IP: str) -> str:
        # dot and colon should not co-exit in one IP
        if ('.' in IP and ':' in IP) or ('.' not in IP and ':' not in IP):
            return "Neither"
        if '.' in IP:
            # check if it valid IPv4
            IP = IP.split('.')
            if len(IP) != 4:
                return "Neither"
            else:
                for i in IP:
                    if not i.isdigit():
                        return "Neither"
                    else:
                        if not 0<=int(i)<=255:
                            return "Neither"
                        if i[0] == '0' and (len(i)!=1):
                            return "Neither"
                return "IPv4"
        else:   
            IP = IP.split(':')
            if len(IP) != 8:
                return "Neither"
            # check if valid IPv6
            else:
               
                for i in IP:
                    if len(i) > 4:
                        return "Neither"
                    if len(i) > 0 and i[0]=='-':
                        return "Neither"
                    try:
                        int(i, 16)
                    except:
                        return "Neither"
                return "IPv6"
            
            
