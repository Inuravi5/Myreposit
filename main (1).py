input_year=int(input("Enter the Year:")) 
if(input_year%400==0):
  print("%d is a leapyear"%input_year)
elif(input_year%100==0):
  print("%d is Not a LeapYear"%input_year)
elif(input_year%4==0):
 print("%d is a Leap Year" %input_year)
else:
 print("%d is Not a LeapYear"%input_year)