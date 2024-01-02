"""
In the United States, it’s customary to leave a tip for your server after dining in a restaurant, typically an amount equal to 15% or more of your meal’s cost.
Not to worry, though, we’ve written a tip calculator for you, below!

...

Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:
- dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
- percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
Assume that the user will input values in the expected formats.
""" 

# This main function gets the input from the user for the meal cost and the tip percentage, and calls the dollars_to_float and percent_to_float functions to calculate the tip, and then prints the tip.
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# This dollars_to_float function accepts a str as input (formatted as $##.##, wherein each # is a decimal digit), removes the leading $, and returns the amount as a float.
def dollars_to_float(dollars):
    return float(dollars.replace("$", ""))
    
# This percent_to_float function accepts a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float.
def percent_to_float(percent):
    return float(percent.replace("%", "")) / 100

main()