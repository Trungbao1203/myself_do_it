current_year = 2024 # kiểu dữ liệu Int

print ( "Your firstname:")
Firstname = input()

print ("Your lastname:")
Lastname = input()

print ("Where you were born?") # kiểu dữ liệu Str
Born = int(input()) # đổi sang Int
Age = current_year - Born # cùng kiểu dữ liệu thì mời TRỪ được

print ("Your name is " + Firstname + " " + Lastname )
print ("You are" + " " + str(Age)) 