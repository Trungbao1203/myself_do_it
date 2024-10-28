class Student:
	def __init__(self,name, age, math_core, liberger_core):
		self.name = name
		self.age = age
		self.math_core = math_core
		self.liberger_core = liberger_core
		self.techer = "Trung Bao"
	def aveger(self):
		aveger = (self.math_core + self.liberger_core)/2
		return aveger
	def print_info(self):
		ave = str(self.aveger())
		print("Student " + self.name + " have math core: " + str(self.math_core) + " liberger core: " + str(self.liberger_core) + " then aveger: " + ave)

s1 = Student("Luan", 24, 7, 8)
s2 = Student("Bao Trieu", 25, 9, 7)
s3 = Student("Thien Sang", 23, 7, 7)
s4 = Student("Kim Phong", 27 , 9, 10)

# s1.print_info()
# s2.print_info()
 
students = []
students.append(s1)
students.append(s2)
students.append(s3)
students.append(s4)

for i in range (len(students)):
	students[i].print_info()