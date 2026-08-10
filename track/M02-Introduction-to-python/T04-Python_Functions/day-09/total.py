def display_invoice_total(price,quantity):
    total = price * quantity
    return total
    pass

price = int(input())
quantity = int(input())
result = display_invoice_total(price,quantity)
print("Total:",result)