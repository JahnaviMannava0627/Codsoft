import os

def show_menu():
    print("1. View To-Do List")
    print("2. Add Item to To-Do List")
    print("3. Update Item in To-Do List")
    print("4. Remove Item from To-Do List")
    print("5. Exit")

def view_list():
    try:
        with open("todo_list.txt", "r") as f:
            todo_list = f.readlines()
            if not todo_list:
                print("Your to-do list is empty.")
            else:
                for index, item in enumerate(todo_list, 1):
                    print(f"{index}. {item.strip()}")
    except FileNotFoundError:
        print("Your to-do list is empty.")

def add_item():
    item = input("Enter the item to add to your to-do list: ")
    with open("todo_list.txt", "a") as f:
        f.write(item + "\n")
    print("Item added to your to-do list.")

def update_item():
    view_list()
    try:
        item_index = int(input("Enter the index of the item to update: ")) - 1
        new_item = input("Enter the new item: ")
        with open("todo_list.txt", "r") as f:
            todo_list = f.readlines()
        todo_list[item_index] = new_item + "\n"
        with open("todo_list.txt", "w") as f:
            f.writelines(todo_list)
        print("Item updated successfully.")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid index.")

def remove_item():
    view_list()
    try:
        item_index = int(input("Enter the index of the item to remove: ")) - 1
        with open("todo_list.txt", "r") as f:
            todo_list = f.readlines()
        removed_item = todo_list.pop(item_index)
        with open("todo_list.txt", "w") as f:
            f.writelines(todo_list)
        print(f"Item '{removed_item.strip()}' removed from your to-do list.")
    except (IndexError, ValueError):
        print("Invalid input. Please enter a valid index.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_list()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
