my_list = [12, 48, 27, 30, 11, 8, 66, 3, 9]
print("Welcome to List Operations Program!")
print("Menu:")
print("1. Add a number to the list")
print("2. Remove a number to the list")
print("3. Insert a number at a specific position")
print("4. Pop a number from the list")
print("5. Find the sum, average, and maximum of the list")
print("6. Search for a number in the list")
print("7. Remove all odd numbers from the list")
print("8. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        add_number = int(input("Enter a number to add: "))
        my_list.append(add_number)
        print("Number added to the list")
    elif(choice == 2):
        remove_number = int(input("Enter a number to remove: "))
        if remove_number in my_list:
            my_list.remove(remove_number)
            print("Number removed from the list!")
        else:
            print("Number not found in this list!")
    elif(choice == 3):
        insert_number = int(input("Enter a number to insert: "))
        position = int(input("Enter the position where you want to insert number: "))
        if 0 <= position <= len(my_list):
            my_list.insert(position, insert_number)
            print("Number inserted in the list")
    elif(choice == 4):
        pop_index = int(input("Enter the index of the number to pop from list: "))
        if 0 <= pop_index < len(my_list):
            pop_number = my_list.pop(pop_index)
            print(f"Number {pop_number} popped from list!")
        else:
            print("Number not found in this list!")
    elif(choice == 5):
        calc_list = str(input("Enter to calculate: "))
        if calc_list == 'sum':
            sum = sum(my_list)
            print(f"Sum of my list: {sum}")
        if calc_list == 'average':
            average = sum(my_list) / len(my_list)
            print(f"Average of the list: {average}")
        if calc_list == 'max':
            max = max(my_list)
            print(f"Maximum of my list: {max}")
        if calc_list == 'min':
            min = min(my_list)
            print(f"Minimum of my list: {min}")
    elif(choice == 6):
        searched_number = int(input("Enter number to search for in the list: "))
        if searched_number in my_list:
            found = (my_list.index(searched_number))
            print(found)
        else:
            print("Number not found in the list")
    elif(choice == 7):
        for odd in my_list:
            if(odd%2 != 0): 
                my_list.remove(odd)
                print("Odd number removed from list!")
        print("All odd numbers removed from list!")
    
    show_list = input("Do you want to see the updated list? (yes/no): ")
    if show_list in ["yes"]:
        print("Updated List:", my_list)
    if show_list in ["no"]:
        print("OK. Moving on.")
    elif(choice >= 8):
        print("Thanks for your contributions to this list! See you soon!")
        break



