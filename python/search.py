def search(arr,n,x):
    for i in range(0,n):
        if (arr[i]==x):
            return i
    return -1

arr=[2,10,3,4,5,6,7]
n=len(arr)
x=10

result=search(arr,n,x)
if result==-1:
    print('not')
else:
    print(result)



def search(arr,n,x):
	for i in range(0,n):
		if arr[i]==x:
			return i
	return -1

arr=[2,54,76,87,34,65,87]
n=len(arr)
x=76
m=search(arr,n,x)
print(arr[m])




arr=[43,65,87,90,54,43,54,76,24,54]
x=54
n=len(arr)
def search(arr,n,x):
    for i in range(0,n):
            if arr[i]==x:
                  return i
    return -1

m=search(arr,n,x)
print(f' values :{arr[m]} at index {m}')
