# Read the limit
limit = int(input("L:"))
#Intialize the loop variable and total
number =1
total = 0
# Examine every number from 1 to limit
while number <= limit:
    if number % 2==0:
        total+=number
    number+=1
# Display the result
print(f"Even Sum: {total}")