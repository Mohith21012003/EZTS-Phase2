stc=[]
def push_element():
    if len(stc)==n:
        print("Stack is full!!!!!!")
    else:
        element=input("Enter the element foe stack:-3")
        stc.append(element)
        print(stc)
def pop_element():
    if not stc:
        print("Stack is empty,add the element")
    else:
        e=stc.pop()
        print(e,"removed")
        print(stc)


n=int(input("Enter the size of stack:"))
while True:
    print("Select the operation: 1.push 2.pop 3.quit")
    choice = int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==2:
        break
    else:
        print("Enter the correct operation !")
