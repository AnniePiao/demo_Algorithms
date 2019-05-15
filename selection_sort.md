# SelectionSort

~~~python
#1st version for selectionSort
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

  

~~~python
#2nd version for selectionSort
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

~~~

- Similarly, **one for finding the minimum index**,**one for sorting**

  

>**L = [7,8,45,6,9,33]**



**for i in range(len(arr)-1):**
		**mini_index = find_mini_index(arr,i)**

>Because of the find_mini_index start with (start+1)—>(i+1)
>
>**in select method**,**the reason for len(arr)-1 is the for loop in find_mini_index is starting from (start+1)**,**which is in order to avoid "out of bounds"**



- searching the mini_index ,—> L = [ 7 , **8 , 45 , 6 , 9 , 33** ] ,finding that 6<7

- Swap these 2 values —>L = [ **6** , 8 , 45 , **7** , 9 , 33 ]



- searching the mini_index ,—> L = [ 6 , 8 ,**45 , 7 , 9 , 33** ] ,finding that 7 < 8
- Swap these 2 values —>L = [  6, **7** , 45 ,**8** , 9 , 33 ]

The running time of this sorting is O(n^2) complexity,it's not a effective method for sorting.

