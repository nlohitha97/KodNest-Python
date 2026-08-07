word = input()
first = int(input())
second =int(input())
third = int(input())
numbers = [first,second,third]
record = (first,second,third)
# Slice the string,list and tuple

m=word[1:-1]
f = numbers[0:2]
r = record[::-1]

print(f"Mddle: {m}")
print(f"First Two Elements: {f}")
print(f"Reversed Tuple: {r}")