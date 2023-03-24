class Student:

    def init(self):
     self.__name = ""
     self.__rollNumber = ""

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    
    def getRollNumber(self):
        return self.__rollNumber


student = Student()
student.setName("habib")
student.setRollNumber("128")
print(student.getName())
print(student.getRollNumber()) 