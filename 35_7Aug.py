import datetime

def ask_yes_no(prompt):
	while True:
		answer = input(prompt)
		if answer == "yes":
			return True
		elif answer == "no":
			return False
		else:
			continue

def calc_age(year_born):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year

	age = CURRENT_YEAR - year_born
	return age
	
def calc_height(meter):
	METER_TO_FEET = 3.281
	feet = meter * METER_TO_FEET
	feet = round(feet,1)
	return feet
def ask_person_info():
	# ask for details from users
	firstname = input("Your firstname: ")
	lastname = input("Your lastname: ")
	year_born = int(input("When you were born: "))
	height_meter = float(input("Your height (meter): "))
	is_male = ask_yes_no("Are you male (yes/no): ")
	is_vietnamese = ask_yes_no("Are you Vietnamese (yes/no): ")
	return firstname, lastname, year_born, height_meter, is_male, is_vietnamese

def print_person_info(firstname, lastname,age,height_feet,is_male, is_vietnamese):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	# print the information of the user after processing using string format, \n is the newline character
	print("\n---")
	print("Your name is " + firstname + " " + lastname)
	print("{2} is {0} years old in {1}".format(age,CURRENT_YEAR,firstname))
	print("You are " + str(height_feet) + " feet tall")

	if is_vietnamese == True:
		print("You are form Vietnamese")
	else:
		print("you aren't form Vietnamese")

	# check height of the user based on their gender
	if is_male == True:
		if height_feet > 6.5:
			print("You are", end=" ")

			# print "very" 10 times using for
			for i in range(10):
				print("very", end=" ")

			print("tall as a man")
		elif height_feet > 6.0:
			print("You are - tall - as a man")
		else:
			print("You are - short - as a man")
	else:
		if height_feet > 5.7:
			print("You are tall as a girl")
		elif height_feet < 5.0:
			print("You are", end=" ")

			# print "very" 10 times using while
			i=0
			while i<10:
				print("very ", end = "")
				i+=1

			print("short as a girl")
		else:
			print("You are - short - as a girl")

def main():
	firstname, lastname, year_born, height_meter, is_male, is_vietnamese = ask_person_info()
	age = calc_age(year_born)
	height_feet = calc_height(height_meter)
	print_person_info(firstname, lastname,age, height_feet, is_male, is_vietnamese)

main()