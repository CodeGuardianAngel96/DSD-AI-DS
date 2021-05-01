top = -1

def push(stack):
	
	global top
	if top == len(stack) - 1:
		
		print("Stack Overflow")
	else:
		element = int(input("Enter the element: "))
		top += 1
		stack[top] = element

def pop(stack):
	
	global top
	
	if top == -1:
		
		print("Stack Underflow")
	else:
		print(stack[top])
		top -= 1

def display(stack):
	
	global top

	if top == -1:
		print("Stack is empty")
	else:
		index = top
		while index >= 0:
			
			print(stack[index])
			index -= 1

def peek(stack):
	global top
	if top == -1:
		print("stack is empty")
		
	else:
		print(stack[top])
		
	
if __name__ == "__main__":

	print("Enter the size of stack: ", end = "")
	size  = int(input())
	stack = [0] * size
	
	option = -1	
	while(option != 0):

		print("******Select a number for operation******")
		print("\t0. Exit")
		print("\t1. Push")
		print("\t2. Pop")
		print("\t3. Display")
		print("\t4. Peek")

		option = int(input("Enter your option: "))
		
		if option == 1:
		    push(stack)
		elif option == 2:
		    pop(stack)
		elif option == 3:
			display(stack)
		elif option == 4:
			peek(stack)
		elif option == 0:
		    break
		else:
		    print("OPTION NOT VALID")
