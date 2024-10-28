CURRENT_YEAR = 2024 # kiểu dữ liệu Int
METER_TO_FEET = 3.281 # hệ số đổi từ Meter sang Feet

Firstname = input("Your firstname: ")
Lastname = input("Your lastname: ")
born = int(input("Where you were born? ")) # đổi sang Int, input đầu vào là String
height_meter = input("Your height (meter): ")

age = CURRENT_YEAR - born # cùng kiểu dữ liệu thì mời TRỪ được
height_meter = float(height_meter)
height_feet = height_meter*METER_TO_FEET
height_feet = round(height_feet,1) #làm tròn, chỉ lấy 1 số sau dấu phẩy

print("\n----")
print ("Your name is " + Firstname + " " + Lastname )
print ("{0} is {1} year old in {2}".format(Firstname,age,CURRENT_YEAR)) 
print ("You are " + " " + str(height_feet) + " " + " feet tall ")

Gender = input("Are you man (yes/no):") #nhập yes no
is_male = None #khởi tạo is_male

if Gender == "yes" or Gender == "y" or Gender == "Y" or Gender == "Yes": # chuyển yes sang kiểu dạng dữ liệu Boolean
	is_male = True
elif Gender == "no" or Gender == "n" or Gender == "N" or Gender == "No":
	is_male = False
else:
	is_male = None # đoạn code phản hồi khi nhập lại các dữ liệu không phải yes no

if is_male == None:
	print("Invalid Answwer ")
elif is_male == True:
	if height_feet >=6.5:
		print("You are very tall as a man")
	elif height_feet >6.0:
		print("You are tall as a man")
	else: 
		print("You are short as a man")
elif is_male == False:
	if height_feet >=6.5:
		print("You are very tall as a girl")
	elif height_feet >6.0:
		print("You are tall as a girl")
	else:
		print("You are short as a girl")
else:
	print("Error")

