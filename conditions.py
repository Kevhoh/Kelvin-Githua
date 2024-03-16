# Python Conditional Statements 
#example is https://plpacademy.powerlearnproject.org/course-module/62fbec9d28ac4762bc524f92/week/62fe1efd28ac4762bc524f9c/lesson/62fe1fbd28ac4762bc524f9f



# Create a Python program that:


# - Prompts a user to enter their age.
# - Uses a conditional statement to check if the age is greater than or equal to 18.
# - Prints "You are eligible to vote" if true, otherwise "You are not eligible to vote."
#This programs keeps asking for age until you quit it yourself
#it also runs to stop all errors in the input
# Function to validate age input
def validate_age(age_str):
    try:
        age = int(age_str)
        if age < 0 or age >100:
            print("The Range should be 0 to 100.")
            return None
        return age
    except ValueError:
        print("Invalid input. Age should be in numbers like 10, 20....")
        return None

# Main program loop
while True:
    print("Enter your age (To quit enter type 'q'): ")
    age_input = input()
    if age_input.lower() == 'q':
        break

    age = validate_age(age_input)
    if age is not None:
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    print()  # Print an empty line for better readability
