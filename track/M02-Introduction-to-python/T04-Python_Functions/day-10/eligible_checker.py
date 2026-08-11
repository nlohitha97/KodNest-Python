def check_eligiblity(marks,attendance,project_completed):
    # TODO:Check whether all three eligibilty conditons are met or not
    
    if marks>60 and attendance>75 and project_completed=="yes":
        return "Eligible"
    else:
        return "Not Eligible"

# Read the student's details
marks = int(input())
attendance = int(input())
project_completed = input() 

# Check the function and print the returned result
result = check_eligiblity(marks,attendance,project_completed)
print(result)