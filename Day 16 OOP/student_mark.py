class Student:
    def _init_(self, name, subject, marks): #initializer method, constructor method
        self.name = name
        self.subject = subject
        self.marks = marks
    def average(self): #method of the class, it is associated with the object of the class
        return sum(self.marks)/len(self.marks)
    @staticmethod  #do not use the self parameter in the static method, it is not associated with the object of the class
    def welcome(): #static method of the class, it is not associated with the object of the class
        print("Welcome to the Student class")
    @staticmethod
    def goodbye():
        print("Goodbye from the Student class")
s1 = Student()
s1._init_("Nabin", "Math", [90, 80, 70])
# print(f"Student name is : {s1.name}")
# print(f"Student subject is : {s1.subject}")
print(f"Student average marks is : {s1.average()}")
s1.welcome()
s1.goodbye()
s2 = Student()
s2._init_("Sita", "Science", [80, 70, 60])
print(f"Student average marks is : {s2.average()}")

# https://www.youtube.com/watch?v=HeW-D6KpDwY