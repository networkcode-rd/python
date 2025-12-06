# Q> how many weeks we have left, if we live until 90 years old?
# Converting 90 years into weeks.
total_week = 4696

#Asking user for current age
current_age = int(input("What is your current age?:"))

#how many weeks have passed till date based on user input. Converting current age into weeks.
# 1 year = 52.1775 wk
week_spent = int(current_age * 52.1775)
# print(week_spent)

def life_in_weeks():
    estimate_weeks_left = total_week - week_spent
    return estimate_weeks_left

weeks_left = life_in_weeks()
print(f"You have {weeks_left} weeks left.")