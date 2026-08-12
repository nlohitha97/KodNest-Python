# Read the number of registration entries
n=int(input("n:"))
# Creating an empty set to store unique student IDs
registrations = set()
# Read and store the Studetn IDs

for _ in range(n):
    student_id = input().strip()

    # TODO: Add the student ID to the set
    registrations.add(student_id)

# Readnthe student ID to search
search_id = input().strip()

# TODO: Calculate the number of uniqur registrations
unique_count = len(registrations)

# TODO: Calculate the number of duplicates entries
duplicate_count = n-unique_count

# Print the counts
print(f"Unique registratins: {unique_count}")
print(f"Duplicate entries: {duplicate_count}")

# TODO: Check whether search_id exists in registraions
if search_id in registrations:
    print("Registered")
else:
    print("Not Registered")