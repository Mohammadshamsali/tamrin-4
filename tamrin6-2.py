class Student:

    def __init__(self, first_name, last_name, age, national_number, student_number,GPA ):
        
        self.first_name = first_name 

        self.last_name = last_name

        self.age = age 

        self.national_number = national_number

        self.student_number =  student_number

        self.GPA = GPA
    
    
    def get_firsr_name(self):
        return ("The first name: "+ self.first_name)
      
    def get_age(self):
        return ("The "+self.first_name + 's age is ' + str(self.age))
    

    
student_1 = Student('Ali', 'SHAMS', 24 ,  99211140162022 , 2124003452 , 16.77)

student_2 = Student('MILAD', 'POORALI', 21 ,  99212240062012 , 2024133458 ,18.50)

student_3 = Student('MOHAMMAD', 'Rahimi', 23 ,  92141140133002 ,'0025086123' , 19.08)



print(student_2.get_age())
print(student_2.get_firsr_name())
