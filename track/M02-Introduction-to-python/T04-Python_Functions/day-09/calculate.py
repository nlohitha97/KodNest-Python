def calculate(a,b,op):
    if op =='+':
        return a+b
    elif op =='-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/'  and b!=0:
        return a/b
    pass
a = int(input("enter a:"))
b = int(input("enter b:"))
op = input("enter the operator:")
print(calculate(a,b,op))