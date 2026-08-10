def check_sign(number):
    if number>0:
        return "Positive"
    elif number<0:
        return "Negative"
    else:
        return "Zero"
    pass

number = int(input())
print(check_sign(number))
