def findSmall(list):
	small = list[0]
	small_index = 0
	for i in range(1,len(list)):
		if list[i]<small:
			small = list[i]
			small_index = i
	return small_index

def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		small = findSmall(arr)
		newArr.append(arr.pop(small))
	return newArr



A = [10,4,2,5,6,8,12]
arr = selectionSort(A)
print(arr)