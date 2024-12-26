# let's create program that will can Identify leap year
def leap_year(year):
    # check it mathematically
    if year % 4 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


# take the year from user
user_year = int(input("Input the year: "))
# call the function
leap_year(user_year)
