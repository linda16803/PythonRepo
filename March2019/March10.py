"""This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2."""

def availList(inputList):
    resultList = [0]
    for x,y in inputList:
        found = 0
        for i in range(len(resultList)):
            if x >= resultList[i]:
                resultList[i] = y
                found = 1
                break
        if found == 0:
            resultList.append(y)
    return len(resultList)

print(availList([(30, 75), (0, 50), (60, 150)]))
