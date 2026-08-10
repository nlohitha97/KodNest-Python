skills = []
# Read and store five skills
for i in range(5):
    skills.append(input())

#  Convert the lists into a tuple
skill_record = tuple(skills)

# Create the required slices
ft = skill_record[:3]
lt = skill_record[3:]
als = skill_record[0:5:2]
rs = skill_record[::-1]

# Display all reqiured results
print(f"Skill Record: {skill_record}")
print(f"First Three: {ft}")
print(f"Last Two: {lt}")
print(f"Alternate: {als}")
print(f"Reverse: {rs}")