class todo:
    def __init__(self,name,):
        self.name=name
        self.to_do=[]
        

    def write(self,):
        print("Hello sir !!! ",self.name,"\nwhat you want to do...\n")
        ch="y"
        while ch=="y":
            task=input()
            self.to_do.append(task)
            ch=input("Want  to add more!!,Y or N").lower()
            if ch != "y":
                break



    def remove(self):
        while True:
            print("\n")
            rm = input("Enter which task you want to remove: ")
            if rm in self.to_do:
                self.to_do.remove(rm)
                print(f"'{rm}' has been removed from your to-do list.")
            else:
                print(f"'{rm}' not found in your to-do list.")
            ch = input("Want to remove more? (Y or N): ").lower()
            if ch != "y":
                break

    def del_whole(self):
        self.to_do.clear()
        print("All tasks have been cleared from your to-do list.")

    def show(self,):
        if(len(self.to_do)==0):
            print("\n")
            print("Sorry  you havent anything To-do! :)")

        else:
            print("\n")
            print(f"Your To-do list for {self.name}")
            for i,task in enumerate(self.to_do):
                print(f"{i+1} {task}")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.to_do:
                file.write(task + '\n')
        print("Tasks have been saved to 'tasks.txt'.")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.to_do = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.to_do = []
        print("Tasks have been loaded from 'tasks.txt'.")

if __name__ == "__main__":
    user_name=input("enter the name")
    user_todo=todo(user_name)
    user_todo.load_tasks()

    while(True):
        print("\n")
        print("1. Add Tod-list")
        print("2. veiw list")
        print("3. Remove")
        print("4. Clear All")
        print("5. Save")


        choice=input("Enter  the  choice:")

        if choice=="1":
            user_todo.write()

        elif choice=="2":
            user_todo.show()

        elif choice=="3":
            user_todo.remove()
        
        elif choice=="4":
            user_todo.del_whole()

        elif choice=="5":
            user_todo.save_tasks()
            break

        else:
            print("Invalid  choice.!!, Please  choose from 1 , 2 and 3 options")
        
