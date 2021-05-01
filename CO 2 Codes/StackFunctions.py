stack = []
# stack using in built functions
def push():

    if len(stack) == n:
        print("stack overflow")

    else:
        print("enter the element:", end ="")
        ele = int(input())
        stack.append(ele)
def pop():

    if not stack:
        print("stack is empty")
    else:
        ele = stack.pop()
        print(ele)

def peep():

    if not stack:
        print("stack is empty")
    else:
        top = len(stack) - 1
        print(top)

def display():
    
    if not stack:
        print("stack is empty")
    else:
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])

n = int(input("Enter the size:"))
while True:

    print("****Menu Option****")
    print("1. Push")
    print("2. Pop")
    print("3. Peep")
    print("4. Display")
    print("5. Exit")
    print("Enter your option:", end = "")

    option = int(input())
    if option == 1:
        push()
    elif option == 2:
        pop()
    elif option == 3:
        peep()
    elif option == 4:
        display()
    elif option == 5:
        exit()
    else:
        print("Option not valid")
        continue
        
