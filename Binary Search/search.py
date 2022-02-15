
def naive(l, target):
    
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1



def binary_search(l, target, low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(l) -1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if  target == l[midpoint]:
        return midpoint

    elif target < l[midpoint]:
        return binary_search(l,target,low,midpoint - 1)

    else: # target > l[midpoint]
        return binary_search(l,target,midpoint + 1,high)

if __name__ == '__main__':
    l = [1,4,8,10,11]
    target = 10

    print(naive(l,target))
    print(binary_search(l,target))