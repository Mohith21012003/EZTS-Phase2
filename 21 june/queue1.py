queue=[]
def enqueue():
    if len(queue)==n:
        print("queue is full!!!!!!")
    else:
        element=input("Enter the element foe stack:")
        queue.append(element)
        print(queue)
def dequeue():
    if not queue:
        print("queue is empty,add the element")
    else:
        e=queue.pop(0)
        print(e,"removed")
        print(queue)


n=int(input("Enter the size of queue:"))
while True:
    print("Select the operation: 1.enqueue 2.dequeue 3.quit")
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==2:
        break
    else:
        print("Enter the correct operation !")
