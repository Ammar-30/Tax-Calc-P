# income = float(input("enter your salary"))
# if income <= 12500:
#     print ("you dont need to pay tax")
# else:
#     tax = (income - 12500)* 0.20
#     net = (income - tax)
#     print ("your tax is",(tax))
#     print ("your net is", (net))

income = float(input("Enter your salary: "))

if income >= 12500 and income <= 50000:
    tax = (income-12500)*0.20
    print("You have to pay the tax", tax)
elif income >= 50000 and income <= 150000:
    tax = (income - 50000)*0.40
    print("You have to pay the tax", tax)
elif income >= 150000:
    tax = (income - 150000)*0.45
    print("You have to pay the tax", tax)
else:
    print("no tax")