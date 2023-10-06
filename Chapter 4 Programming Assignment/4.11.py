#4.11
#Find the number of days in a month
#Abdullah Mohammad
#1/5/23


# 1 Jan = 31
# 2 Feb = 28 (in normal) 29 (in leap)
# 3 Mar = 31
# 4 Apr = 30
# 5 May = 31
# 6 Jun = 30
# 7 Jul = 31
# 8 Aug = 31
# 9 Sep = 30
#10 Oct = 31
#11 Nov = 30
#12 Dec = 31

month = eval(input("Enter a month number (Jan=1, Feb=2, etc.): "))
year = eval(input("Enter a year: "))

isLeapYear = year%4 == 0


if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    DayNum = 31
elif month == 2:
    DayNum = 29 if isLeapYear else 28
else:
    DayNum = 30


print("January" if month==1 else "February" if month==2 else "March" if month==3 else "April" if month==4 else "May" if month==5 else "June" if month==6 else "July" if month==7 else "August" if month==8 else "September" if month==9 else "October" if month==10 else "November" if month==11 else "December", end =', ')
print(year, end=' ')
print("has", DayNum, "days")


    
