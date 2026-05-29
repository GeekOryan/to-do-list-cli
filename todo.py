

import json
from operator import itemgetter

'''
What does one task look like?
1. A name/description
2. A due date
3. A priority
4. A status (Pending/Complete)

# task = {"name": "", "due": "", "priority":"", "status": "pending"}

'''

tasks = []

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            loaded_data = json.load(file)
            return loaded_data
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# save_tasks([{"test": "data"}])


def main():
    tasks = load_tasks()
    print("Welcome back. Loading your data...")
    
    while(True):
        print("----- TO_DO LIST MENU -----")
        print("1. Add: ")
        print("2. View: ")
        print("3. Complete ")
        print("4. Delete: ")
        print("5. Exit: ")
        
        choice = input("Enter your choice (1 - 5): ")
        
        if choice == '1':
            print("Add task feature : coming soon")
        elif choice == '2':
            if not tasks:
                print("No tasks found")
                continue
            sort_choice = input("View By: 1. Due Date 2. Priority: ")
            
            display_tasks = tasks.copy()
        
        
            if sort_choice == '1':
                display_tasks.sort(key=itemgetter('due'))
            elif sort_choice == '2':
                display_tasks.sort(key=itemgetter('priority'))
            else:
                print("Invalid input. Please select 1 or 2")
                
            task_number = 1
            
            for display_task in display_tasks:
                name_value = display_task['name']
                due_value = display_task['due']
                priority_value = display_task['priority']
                status_value = display_task['status']
                
                print(f"{task_number}. {name_value} | Due: {due_value} | Priority: {priority_value} | Status: {status_value} ")
                task_number += 1
        elif choice == '3':
            print("Complete task feature : coming soon")
        elif choice == '4':
            print("Delete task feature : coming soon")
        elif choice == '5':
            print("Goodbye!")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select a valid option (1 - 5)")


main()