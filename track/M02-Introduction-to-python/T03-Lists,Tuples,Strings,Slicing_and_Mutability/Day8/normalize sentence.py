# Read the sentence
sentence = input()

# Remove spaces from the beginning and end
clean = sentence.strip()

# Convert the sentence to lowercase
norm = clean.lower()

# Remove all full stops
norm = norm.replace(".", "")

# Split the normalized sentence into words
word = norm.split()

# Join the words using a hyphen
slug = "-".join(word)

# Convert the normalized sentence to uppercase
up = norm.upper()

# Find the starting index of the word "python"
pos = norm.find("python")

# Display all the processed results
print(f"Cleaned: {clean}")
print(f"Normalized: {norm}")
print(f"Words: {word}")
print(f"Slug: {slug}")
print(f"Uppercase: {up}")
print(f"Python Position: {pos}")