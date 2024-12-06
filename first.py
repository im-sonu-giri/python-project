print("welcome to the tip calculator  ")
total_amount=float(input("what was the total bill ?"))
tips = int(input("what percentage tip would you like to give"))
split_bill = int(input("how many people to split the bill?"))
tip_percent = (total_amount * tips)/100
pay_by_each_person = (tip_percent+total_amount)/split_bill
print(pay_by_each_person)