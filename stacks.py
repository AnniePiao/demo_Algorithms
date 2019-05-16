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


