# Read the number of students
student_count = int(input())

# Initialize total marks and counters
total_marks = 0
passed_count = 0
failed_count = 0

# Repeat for each student
for i in range(student_count):

    # Read the mark of the student
    mark = int(input())

    # Add the mark to the total
    total_marks = total_marks + mark

    # Check whether the student passed
    if mark >= 40:
        passed_count = passed_count + 1
    else:
        failed_count = failed_count + 1

# Display the total marks
print(f"Total Marks: {total_marks}")

# Display the number of passed students
print(f"Passed Students: {passed_count}")

# Display the number of failed students
print(f"Failed Students: {failed_count}")

# Check the overall batch result
if failed_count == 0:
    print("Batch Result: All Passed")
else:
    print("Batch Result: Needs Improvement")