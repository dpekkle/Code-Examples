"""A program that allows you to calculate the amount of interest on a certain amount
   of money, with room for input of principal (p), number of years deposited (t),
   annual interest rate (r), and rate of compounding (n)"""

from sys import exit
   
print "\nThis program will calculate interest from savings."
print "Please enter the starting value you have / are investing."
principal = float(raw_input("> "))

print "Are you saving for days, weeks, months, or years?"
units_of_time = raw_input("> ")

if units_of_time == "days":
	units_value = float(1.00/365.00)

elif units_of_time == "weeks":
	units_value = float(7.00/365.00)

elif units_of_time == "months":
	units_value = float(30.50/365.00)

elif units_of_time == "years":
	units_value = float(1)

else:
	exit(0)
	
print "How many %s are you saving?" % units_of_time
time = float(raw_input("> "))

print "What is the current interest rate p.a. (e.g. 5.51%)."
raw_rate = float(raw_input("> "))

print "Please enter how many times per year interest is calculated."
print "(Ubank is daily and thus 365)."
annual_compounds = float(raw_input("> "))


rate = raw_rate / 100.000000

end_money = float(principal * (1 + (rate / annual_compounds))**(annual_compounds * time * units_value))
#end_money = (6000 * ( 1 + (5.51 / 100.000000)/1 ** (365 * 1)

interest = float(end_money - principal)

print "The total amount of money after %d %s of interest is $%.2f." % (time, units_of_time, end_money)
print "In that period you have earned $%.2f interest." % interest