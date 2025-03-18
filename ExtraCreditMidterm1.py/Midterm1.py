# ==============================
# BASE CODE: Student Management
# ==============================

STUDENTS = []          
SCORES = []            
BEST_STUDENT_NAME = None
BEST_STUDENT_SCORE = None

def get_best_student_index():
    """
    Returns the index of the student with the highest score,
    or -1 if no students exist.
    """
    
    searched_student_score = int(input("Enter a Student to search for in the list: "))
    if searched_student_score in STUDENTS:
        found = (SCORES.index(searched_student_score))
        print(found)
    #
    pass

def get_highest_score():
    """
    Returns the highest score among SCORES as an integer, or None if empty.
    """
    global STUDENTS, SCORES
    if len(SCORES) == 0:
        return None
    elif len(SCORES) != 0:
        return max(SCORES)
    # TODO 2: Return None if SCORES is empty, else max(SCORES).
    pass

def get_lowest_score():
    """
    Returns the lowest score among SCORES as an integer, or None if empty.
    """
    global STUDENTS, SCORES
    if SCORES == 0:
        return None
    else:
        return min(SCORES)
    # TODO 3: Return None if SCORES is empty, else min(SCORES).
    pass

def calculate_average_score():
    """
    Returns the average (float) of SCORES, or None if SCORES is empty.
    """
    global STUDENTS, SCORES
    if len(SCORES) == 0:
        return None
    elif len(SCORES) != 0:
        return average(SCORES)
    # TODO 4: If SCORES is empty, return None, else sum(SCORES)/len(SCORES).
    pass

def add_student():
    """
    Prompts for a student's name and a valid score [0..100],
    then updates STUDENTS and SCORES.
    Finally, updates BEST_STUDENT_NAME and BEST_STUDENT_SCORE
    based on get_best_student_index().
    """

    global STUDENTS, SCORES, BEST_STUDENT_NAME, BEST_STUDENT_SCORE
    add_student = str(input("Enter a student's name: "))
    add_score = int(input("Enter student's score: "))
    STUDENTS.append(add_student)
    SCORES.append(add_score)
    print("Student added")
    # TODO 5:
    #  - Prompt for name (non-empty).
    #  - Prompt in a loop for a valid score (0..100).
    #  - Append to STUDENTS and SCORES.
    #  - Recalc best student index -> update BEST_STUDENT_NAME, BEST_STUDENT_SCORE.
    pass

def remove_student():
    """
    Removes a student by name from STUDENTS and SCORES.
    If the removed student was the best, recalc the best student index.
    """
    global STUDENTS, SCORES, BEST_STUDENT_NAME, BEST_STUDENT_SCORE
    remove_student = str(input("Enter a student's name: "))
    remove_score = int(input("Enter student's score: "))
    if remove_student in STUDENTS:
        STUDENTS.remove(remove_student)
        print("Student removed from class.")
    else:
        print("Student not found in class.")
    
    if remove_score in SCORES:
        SCORES.remove(remove_score)
        print("Score removed from class.")
    else:
        print("Score not found in class.")
        
    # TODO 6:
    #  - Prompt for the student's name to remove.
    #  - If not found, print "Student not found."
    #  - If found, remove from both lists.
    #  - Recalc best student index -> update BEST_STUDENT_NAME, BEST_STUDENT_SCORE.
    pass

def display_students():
    """
    Prints each student's name and score, labeling as Passing/Failing.
    (Optional) Indicate best student with "[BEST]".
    If no students, print a message.
    """
    if len(STUDENTS) == 0:
        print("No Students to display.")
    for i in range (len(STUDENTS)):
        print(STUDENTS)
        print(SCORES)
        
    # TODO 7:
    #  - If STUDENTS is empty, print "No students to display" and return.
    #  - For each i in range(len(STUDENTS)):
    #       name, score, passing/failing label
    #       if name == BEST_STUDENT_NAME, optionally add "[BEST]"
    pass

def calculate_statistics():
    """
    Prints overall stats using get_highest_score(), get_lowest_score(), 
    and calculate_average_score().
    If no students, print "No data."
    """
    if len(STUDENTS) == 0:
        print("No Data.")
    for i in range(len(STUDENTS)):
        get_highest_score = max(SCORES)
        get_lowest_score = min(SCORES)
        calculate_average_score = sum(SCORES)/len(SCORES)
        print(get_highest_score)
        print(get_lowest_score)
        print(calculate_average_score)

    print
    # TODO 8:
    #  - If no students, print "No data." and return.
    #  - highest = get_highest_score()
    #  - lowest  = get_lowest_score()
    #  - average = calculate_average_score()
    #  - Print them in a neat format (e.g., 2 decimals for average).
    pass

def main():
    """
    Main function: initializes data, then provides a menu until the user chooses to exit.
    """
    
    while True:
        print("\n=== Student Management Menu ===")
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Calculate statistics")
        print("4. Remove a student")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            calculate_statistics()
        elif choice == "4":
            remove_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


