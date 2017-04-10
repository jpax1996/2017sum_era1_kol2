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
from __future__ import division

def interface():
        print "1) Insert new class"
        print "2) Insert New Student in database"
        print "3) Change students attendance"
        print "4) Insert Score to student"
        print "5) Get classe's total average score"
        print "6) Get students average score in class"
        print "7) Count average from every class"
        print "8) Exit"
        print "Chose your number :"
	

def get_inpu():
        in_put = 0
        while in_put < 1 or in_put > 8:
                interface()
                in_put = input()
                return in_put 

def insert_class(newclass):
        classroom[newclass] = []

	
classroom = {}

in_put = 0
while in_put != 8 :
        in_put = get_inpu();
        if in_put == 1:
                print "Please insert name of new class:"
                new_class = raw_input()
                classroom[new_class] = {}
                print (classroom)
        elif in_put == 2:
                print"Please insert name of new student:"
                new_student = raw_input()
                print "Please insert name of classroom"
                new_class = raw_input()
                classroom[new_class][new_student]= {'attendance':[],'grades':[]}
        elif in_put == 3:
                print "Please insert name of class:"
                classe = raw_input()
                print"Please insert name of student:"
                student = raw_input()
                print"Please insert the students attendance (pres/abs):"
                att = raw_input()
                classroom[classe][new_student]['attendance'].append(att)
        elif in_put == 4:
                print "Please insert name of class:"
                classe = raw_input()
                print"Please insert name of student:"
                student = raw_input()
                print"Please grade:"
                grade = input()
                classroom[classe][new_student]['grades'].append(grade)
                
        elif in_put == 5:
                cpt = 0
                som = 0
                classe = raw_input("Please insert name of class:")
                for student in classroom[classe][student]:
                        for grade in classroom[classe][student]['grades']:
                                cpt += 1
                                som += grade
                avg = som/cpt
                print "The average of the student is:"
                print (avg)
        elif in_put == 6:
                cpt = 0
                som = 0
                classe = raw_input("Please insert name of class:")
                student = raw_input("Please insert name of student:")
                for grade in classroom[classe][student]['grades']:
                        cpt += 1
                        som += grade
                avg = som/cpt
                print "The average of the student is:"
                print (avg)
        elif in_put == 7:
                cpt = 0
                som = 0
                for classe in classroom[classe]:
                        for student in classroom[classe][student]:
                                for grade in classroom[classe][student]['grades']:
                                        cpt += 1
                                        som += grade
                avg = som/cpt
                print "The average of the student is:"
                print (avg)
        print(classroom)
	
