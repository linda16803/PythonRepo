
"""
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.

"""


def decode(encodeStr):
    str1 = []
    for i in range(len(encodeStr)):
        num = int(encodeStr[i]) if i%2 == 0 else str1.append(num*encodeStr[i])
    return ("".join(str1))

def encode(decodeStr):
    str1 = []
    num = 1
    for i in range(1,len(decodeStr)):
        if decodeStr[i-1] == decodeStr[i]:
            num +=1
        else:
            str1.append(str(num)+decodeStr[i-1])
            num = 1
    return (''.join(str1))
            

print(encode("AAAABBBBDDDDAAARRRDDDD"))
print(decode("4Y6T3C2J1A8U"))