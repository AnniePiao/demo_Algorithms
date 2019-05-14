# SelectionSort

~~~python
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
~~~

- findSmall method : finding the index of the smallest number in an array and return the index

- selectionSort method : return an selected new array

  

  

## findSmall method

A = [10,4,2,5,6,8,12]

- Assuming that list[0]=10 small_index = 0

- using for loop to the array of [4,2,5,6,8,12] which is except the index 0
- list[i] will become the smallest one while comparing its value with list[0] —> small = list[i] and update the index as well
- return the smallest index 



## selectionSort method

- Firstly,creating a new array for storing the updated data
- Assign the value of the smallest index to small variable
- Pop the smallest value from original array then append the element into the newArr
- Everytime finding the smallest one in the current array(<—reason for using for loop) and update it into the newArr(<—pop and append them one by one)