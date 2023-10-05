

def findMajorityElement(nums):
    d = {}
    for i in nums:
     d[i] = d.get(i,0) + 1
    for key, value in d.items():
        if value > len(nums)/2:
            return key
    return -1
if __name__=='__main__':
        nums = [1,8,7,4,1,2,2,2,2,2,2]
        result = findMajorityElement(nums)
        if result !=-1:
            print('El elemento mayoritario es', result)
        else:
            print('Este elemento mayoritario no existe')
            