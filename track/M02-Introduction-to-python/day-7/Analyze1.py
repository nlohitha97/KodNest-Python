# Read how many numbers will be entered
T = int(input())  #5
# Intialize the counters and total
p=0
n=0
z=0
t=0
# Read and analyze each number
for i in range(T):
    num = int(input())
    t+=i
    if num>0:
        p+=1
    elif num<0:
        n+=1
    else:
        z+=1
    
# Display the final analysis
print("Posithe:",p)
print("Nagative:",n)
print("Zero:",z)
print("Total: ",t)
        