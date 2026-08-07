# Read the course details
course_name = input()
current_week = input()
current_status = input()

# Create the original tuple
course_details = (course_name,current_week,current_status)

# Read the updated week
updated_week = input()

# Create and assign a new tuple
new_course = (course_name,updated_week,current_status)

# Display the updated tuple
print(new_course)