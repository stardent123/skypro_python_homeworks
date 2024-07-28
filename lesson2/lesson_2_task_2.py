def is_year_leap(year):
    if (year % 4 == 0):
        print("year: " + str(year) + " True")
    else:
        print("year: " + str(year) + " False")


is_year_leap(int(input("type a year: ")))