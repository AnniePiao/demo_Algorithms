def find_mini_index(arr,start):
	mini_index = start

	for i in range(start+1,len(arr)):
		if arr[mini_index]> arr[i]:
			mini_index = i
	return mini_index

def select(arr):
	for i in range(len(arr)-1):
		mini_index = find_mini_index(arr,i)
		temp = arr[i]
		arr[i] = arr[mini_index]
		arr[mini_index] = temp
	return arr


L = [7,8,45,6,9,33]
newarr=select(L)
print(newarr)
