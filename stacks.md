# Stacks

- Only the **top element** could be accessible
- (LIFO) Last-in,first-out

seems like putting cards into a vertical box,the first card we put into which could be at the bottom of the box.However,the last one we put into it is at the top.

- Insert —>push
- Delete—>pop

## Stacks code

![](/Users/xinying/Desktop/Python/data structrue/code_for_stack.png)



~~~python
def check_empty(S):
	top = len(S)-1
	mark = False
	if top == -1:
		mark = True
	return mark

def push(S,x):
	S.append(x)
	print S
  
def pop(S):
	if check_empty(S):
		print 'underflow'
	else:
		S.pop(len(S)-1)
		print S


S =[2,13,7,22]
A =[]

pop(A)
pop(S)
pop(S)
push(S,8)



~~~



## Stacks runtime

- All stack operations take time O(1)