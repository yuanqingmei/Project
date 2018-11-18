def total(invoice):
    #assert isinstance(invoice,list):
    sum = 0
    for price,quantity in invoice:
        sum += price * quantity
    return sum

inv1 = [[2.10,12.4],[1.25,2.44],[17.34,3.6]]
print("Total price:", round(total(inv1),2))