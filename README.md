# Introduction-to-Big-Data-Analytics-Group-8
## Group Assignmment

## Group Members
1. Mushimiyumukiza Blaise 26229
2. Izabayo Divine 27813
3. Uwamahoro Christa 25869
4. Ishimwe Joyeuse 26756
5. Genga Chris 27344
6. Muhirwa David 27436






# Question I

# Function to input student information
def input_student_info():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grades = []
    
    number_of_courses = int(input("Enter number of courses (2 or 3): "))
    for i in range(number_of_courses):
        grade = float(input(f"Enter grade for course {i + 1}: "))
        grades.append(grade)
    
    return name, age, grades

# Function to calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function to display student information
def display_student_info(name, age, grades, average):
    print("\n--- Student Report ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Grades: {grades}")
    print(f"Average Grade: {average:.2f}")


def main():
    name, age, grades = input_student_info()
    average = calculate_average(grades)
    display_student_info(name, age, grades, average)


main()


![IMG-20250627-WA0011](https://github.com/user-attachments/assets/debbe5ad-250c-4f32-a753-7d7032417b46)


# Question II

 def is_palindrome(text):
 return text== text[::-1]
 def main():
    user_input = input("\nEnter a string to check if it's a palindrome: ")
    if is_palindrome(user_input):
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")


main()

![IMG-20250627-WA0012](https://github.com/user-attachments/assets/bb5eba08-2b48-414b-aa69-b3b09d3e9a1a)
