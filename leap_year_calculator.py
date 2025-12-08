random_year = int(input("Enter the year: "))
def is_leap_year(random_year):
    if random_year % 400 == 0:
        return True
    elif random_year % 100 == 0:
        return False
    elif random_year % 4 == 0:
        return True
    else:
        return False
    
print(is_leap_year(random_year))