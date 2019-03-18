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