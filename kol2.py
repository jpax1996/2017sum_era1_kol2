#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

def interface():
	print "1) Insert New Student in database"
	print "2) Change students attendance"
	print "3) Insert Score to student"
	print "4) Get students total average score"
	print "5) Get students average score in class"
	print "6) Count total attendance of student"
	print "7) Exit"
	print(Chose your number :)
	

def get_input():
	input = 0
	while input<1 || input>7 :
		interface()
		input = raw_input();
	return input 

def insert_student()

class student_info:
	student_attendance = []
	student_grades = [] []

class classroom:
	number_students = 0
	students = []
	def insert_student(self,name):		
		self.students[self.number_students] = name
		self.number_students += 1
	
database_classroom = classroom
database_student = student_info

input = 0

	while input != 7:
		input = get_input();
		if(input == 1){
			print(Please insert name of new student:)
			new_student = raw_input()
			database_classroom.insert_student(new_student) 		
		}elif(input == 2){
		
		}elif(input == 3){
		
		}elif(input == 4){
		
		}elif(input == 5){
		
		}elif(input == 6){
		
		}
