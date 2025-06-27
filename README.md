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
