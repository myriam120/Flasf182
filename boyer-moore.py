
def findMajorityElement(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    for key, value in d.items():
        if value > len(nums) / 2:
            return key
    return -1

if __name__ == '_main_':
    num_datos = int(input("Ingrese la cantidad de datos: "))
    nums = []
    for _ in range(num_datos):
        dato = int(input("Ingrese el dato: "))
        nums.append(dato)
    
    result = findMajorityElement(nums)
    if result != -1:
        print('El elemento mayoritario es', result)
    else:
        print('No existe un elemento mayoritario')
        
        