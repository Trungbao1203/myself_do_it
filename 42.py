user_input = int(input("Nhap so : " + ""))
print(user_input)

with open("data_42.txt", "w") as file:
	for i in range (user_input):
		file.write(str(user_input - i) + "\n")

with open("data_42.txt", "r") as file:
	numbers = file.read().split() # split là in ra dưới dạng bảng
	print(numbers)

for i in range(len(numbers)): # không sử dụng uner_input vì đề bài yêu cầu sử dụng từ mảng
		print("Line " + str(i+1) + ": " + numbers[i]) 
