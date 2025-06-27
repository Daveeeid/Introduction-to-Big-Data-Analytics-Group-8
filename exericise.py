
# Q1. Student Grade Calculator 
def input_student_info():
    # Collect basic student information
    name = input("Enter student's name: ")  # Get student name as string
    age = int(input("Enter student's age: "))  # Get age as integer
    grades = []  # Initialize empty list to store grades
    
    # Get number of courses and validate input (expecting 2 or 3)
    number_of_courses = int(input("Enter number of courses (2 or 3): "))
    
    # Loop through each course to get grades
    for i in range(number_of_courses):
        grade = float(input(f"Enter grade for course {i + 1}: "))  # Get grade as float
        grades.append(grade)  # Add grade to the list
    
    return name, age, grades  # Return all collected data

def calculate_average(grades):
    # Calculate average by dividing sum of grades by count
    return sum(grades) / len(grades)  # Returns a float value

def display_student_info(name, age, grades, average):
    # Display formatted student report
    print("\n--- Student Report ---")  # Section header
    print(f"Name: {name}")  # Display student name
    print(f"Age: {age}")  # Display student age
    print(f"Grades: {grades}")  # Display list of grades
    print(f"Average Grade: {average:.2f}")  # Display average with 2 decimal places

def main():
    # Main program execution flow
    name, age, grades = input_student_info()  # Step 1: Get student info
    average = calculate_average(grades)  # Step 2: Calculate average
    display_student_info(name, age, grades, average)  # Step 3: Display results

main()  # Start the program execution

# Q2. Palindrome Checker 
def is_palindrome(text):
    """Check if the input string is a palindrome (reads same backward)."""
    # Remove spaces and convert to lowercase for accurate comparison
    clean_text = text.replace(" ", "").lower()
    # Compare the string with its reverse
    return clean_text == clean_text[::-1]

def check_palindrome():
    # Get user input and check if it's a palindrome
    user_input = input("\nEnter a string to check if it's a palindrome: ")
    
    # Check palindrome status and print result
    if is_palindrome(user_input):  # Now properly defined
        print("Yes, it is a palindrome")  # Positive result
    else:
        print("No, it is not a palindrome")  # Negative result

check_palindrome()  # Run the palindrome checker