# 1. Functions with Multiple Parameters: Detailed Explanation

# BMI (Body Mass Index) Calculation
def bmi(weight, height):
    # Parameter validation: checks that the data falls within realistic ranges
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None  # Conditional return if parameters are invalid
    return weight / height ** 2  # International standard formula: weight / height²

# Usage examples:
print(bmi(70, 1.75))  # Normal weight. Approximate Output: 22.86
print(bmi(300, 1.80)) # Data out of range. Output: None


# Unit Conversion System
def lb_to_kg(lb):
    return lb * 0.45359237  # 1 pound = 0.45359237 kg

def ft_and_inch_to_m(ft, inch=0.0):  # Optional parameter with a default value
    return ft * 0.3048 + inch * 0.0254  # 1 foot = 0.3048 m, 1 inch = 0.0254 m

# Important design features of this system:
# 1. Optional parameter: 'inch' defaults to 0.0, allowing it to be omitted during calls.
# 2. Precision: Uses exact conversion factors from the International System of Units.
# 3. Unit combination: Allows converting feet and inches into meters simultaneously.

# Integrated usage of multiple functions:
# Example: Convert 176 pounds to kg and 5 feet 7 inches to meters, then calculate BMI
converted_weight = lb_to_kg(176)
converted_height = ft_and_inch_to_m(5, 7)
print(bmi(converted_weight, converted_height))


# 4. Best Practices and Design Recommendations
# - Single Responsibility Principle: Each function should focus on a single, well-defined task.
# - Input Validation: Verify logical boundaries and return None or raise exceptions for anomalies.
# - Meaningful Naming: Use descriptive and clear identifiers (e.g., ft_and_inch_to_m).

# Practical Example of a Well-Structured Function:
def calculate_compound_interest(principal, rate, years, compounds_per_year=12):
    """
    Calculates compound interest.
    
    Args:
        principal: Initial amount of money (float)
        rate: Annual interest rate in decimal format (float)
        years: Number of investment years (int)
        compounds_per_year: Times interest is compounded per year (default 12)
    
    Returns:
        Calculated future value or None if any input is invalid
    """
    if principal <= 0 or rate < 0 or years < 0 or compounds_per_year < 1:
        return None
    
    return principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)