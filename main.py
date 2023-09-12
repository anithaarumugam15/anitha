#write a program that determines whether a year entered by the user in a LeapYear or not using if_elief_else statement
def isLeapYear(Year):
 if (Year % 4 == 0 and Year % 100 !=0)or year % 400 == 0:
  return True
 else:
  return False

year = int(input("Enter a year:"))

if isLeapYear(year):
  print('{}is a Leapyear.'.format(year))
else:
  print ('{}is not a leapyear.'. format(year))