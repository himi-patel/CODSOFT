task_list=[]

def add_task():

    task_count=int(input("\nhow many task you want to add="))

    for i in range(task_count):
        task_Add=input("\nenter the task :")
        task_list.append({"task":task_Add,"done":False})
        print("task added successfully\n")

        


def view_task():

    print("\nYour tasks:")

    for i,task in enumerate(task_list,1):
        print(f"{i}. {task['task']} - {'Completed' if task['done'] else 'Not Completed'}\n")

def mark_task_completed():

    task_number=int(input("\nenter the task number you want to mark as completed="))

    if task_number>len(task_list):
        print("Invalid task number.")
        return

    task_list[task_number-1]["done"]=True
    print("Task marked as completed successfully\n")
def delete_task():

    task_number=int(input("\nenter the task number you want delete="))

    if task_number>len(task_list):
        print("Invalid task number.")
        return

    task_list.pop(task_number-1)
    print("Task deleted successfully\n")


while True:
    print("\n************To-Do List************\n")



    
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

    print("\n-------------------------------------------\n")




    choice=int(input("\nenter your choice="))

    if choice not in[1,2,3,4,5]:
        print("Invalid choice. please select a valid operation.")
        exit()

    if choice==1:
    
        add_task()
    
    elif choice==2:

        view_task()
    elif choice==3:
        mark_task_completed()

    elif choice==4:
        delete_task()

    elif choice==5:
        print("Thank you for using the To-Do List!")
        exit()
