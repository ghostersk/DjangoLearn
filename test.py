from datetime import date

def check_age(birth_date):
    datex = date.fromisoformat(birth_date)
    today = date.today()
    i = today - datex
    # 6575 days ~ 18 years
    if (i.days > 6575):
        return True
    
    return False

print(check_age("2011-03-01"))