
# Q1. Student Information System

def input_student_info():
    # Prompt user to enter student's name and store as string
    name = input("Enter student's name: ")
    # Prompt user to enter student's age and convert to integer
    age = int(input("Enter student's age: "))
    # Create empty list to store grades
    grades = []
    
    # Ask for number of courses (expecting 2 or 3) and convert to integer
    number_of_courses = int(input("Enter number of courses (2 or 3): "))
    # Loop through each course to collect grades
    for i in range(number_of_courses):
        # Prompt for each grade and convert to float
        grade = float(input(f"Enter grade for course {i + 1}: "))
        # Add each grade to the grades list
        grades.append(grade)
    
    # Return collected information as a tuple
    return name, age, grades

def calculate_average(grades):
    # Calculate average by dividing sum of grades by number of grades
    return sum(grades) / len(grades)


def display_student_info(name, age, grades, average):
    # Print report header
    print("\n Student Report ")
    # Display student's name
    print(f"Name: {name}")
    # Display student's age
    print(f"Age: {age}")
    # Display all grades
    print(f"Grades: {grades}")
    # Display calculated average with 2 decimal places
    print(f"Average: {average:.2f}")


def main():
    # Get student info by calling input_student_info()
    name, age, grades = input_student_info()
    # Calculate average grade
    average = calculate_average(grades)
    # Display all student information
    display_student_info(name, age, grades, average)


# Start the student information program
main()

# Q2. Palindrome Checker

def is_palindrome(text):
    # Check if text equals its reverse (using slicing [::-1])
    return text == text[::-1]

def main():
    # Prompt user to input a string
    user_input = input("\nEnter a string to check if it's a palindrome: ")
    # Check if input is palindrome using is_palindrome() function
    if is_palindrome(user_input):
        # Print if palindrome
        print("Yes, it is a palindrome")
    else:
        # Print if not palindrome
        print("No, it is not a palindrome")

# Start the palindrome checker program
main()
