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