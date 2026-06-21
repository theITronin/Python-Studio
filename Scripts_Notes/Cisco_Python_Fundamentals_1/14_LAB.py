# ==============================================================================
# FILE: Syntax 14. LAB.py
# ==============================================================================

# 1. Function to Determine Leap Years
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

# Leap Year Logic:
# 1. A year is NOT a leap year if it is not divisible by 4 (year % 4 != 0)
# 2. If it is divisible by 4 but not by 100, it IS a leap year
# 3. If it is divisible by 100 but not by 400, it is NOT a leap year
# 4. If it is divisible by 400, it IS a leap year

# Automated Test Data
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
# - 1900: Not a leap year (divisible by 100 but not by 400)
# - 2000: Leap year (divisible by 400)
# - 2016: Leap year (divisible by 4 but not by 100)
# - 1987: Not a leap year (not divisible by 4)


# 2. Function for Days in a Month
def days_in_month(year, month):
    # Returns None for invalid inputs or years prior to the Gregorian calendar
    if year < 1582 or month < 1 or month > 12:
        return None
    
    # List containing the corresponding days for each month
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Dynamic adjustment for February in case of a leap year
    if month == 2 and is_year_leap(year):
        return 29
        
    return days[month - 1]

# Test Cases:
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results_days = [28, 29, 31, 30]


# 3. Day of the Year
def day_of_year(year, month, day):
    # Initial validations
    if year < 1582 or month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None
    
    total_days = 0
    # Sums the days of the previous full months
    for m in range(1, month):
        total_days += days_in_month(year, m)
    # Sums the elapsed days of the current month
    total_days += day
    return total_days

# Execution example:
print(day_of_year(2000, 12, 31))  # Output: 366 (leap year)


# 4. Function for Prime Numbers (with correction)
def is_prime(num):
    if num < 2:
        return False
    # Optimized by evaluating divisibility up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True