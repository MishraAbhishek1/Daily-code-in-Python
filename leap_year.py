# check year is leap or not >>
year = int(input("Enter the any number of year"))

# divided by 100 means century year (ending with 00)
#Century year is divided by 400 is leap yeaar

if(year % 400 == 0)and (year % 100 == 0):
    print("{0} is a leap year".format(year))
    
#not divided by 100 means not a century year >>
# Year is divided by 4 is a Leap Year >>

elif(year %4 == 0) and (year % 100 != 0):
    print("{0} is leap year".format(year))
    
# if not divided by both 400 (century year)and 4 (not a century year)
# year is not aleap year >>

else:
    print("{0} is not a leap year".format(year))        
