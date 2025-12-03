bill = float(input("What is the total bill in Rs.?\n"))
tip_percentage = int(input("What is the tip percentage? Recommended 10 or 12 or 15\n"))
splitting_bill_between = int(input("How many are contributing?\n"))
payment_method = str(input("What is your mode of payment? Card/Online/Cash\n"))

calculating_total_bill_including_tip = (bill * tip_percentage / 100 )+ bill
bill_per_person = round(calculating_total_bill_including_tip / splitting_bill_between, 2)

if payment_method == "Cash":
    print(round(bill_per_person))
else:
    print(f"Each person has to pay Rs.{bill_per_person}")