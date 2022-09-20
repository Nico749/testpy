# calculate the monthly payment of a mortgage
def calculateMortgage(amount,rate,numberPayments):
    num = (rate*(1+rate)**numberPayments)
    denom = ((1+rate)**numberPayments)-1
    payment = amount*(num/denom)
    print("the payment is ",payment)
    


calculateMortgage(100000,0.005,180)

