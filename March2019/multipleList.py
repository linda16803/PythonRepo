"""
Given a list of integer, get a result list which 
is multiple all other values inside list except itself.
"""


from functools import reduce
li = [5,8,10,20,50,4]
mul = reduce((lambda x,y: x*y), li)
result=list(map(lambda x: int(mul/x), li))

print(result)