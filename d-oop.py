
class Student:
    """
    This __init__ is a constructor - here is the equivalent Java code:
    public Student (String name, String location) {
        this.name = name;
    }
    """
    def __init__(self, first_name, last_name, location):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
    
    # all methods are always public - no notion of private
    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def _get_location(self):
        return self.location

# Student my_student = new Student(name, location...) <- Java equivalent
my_student = Student("Aidan", 'Melvin', 'South Campus Commons')
print(my_student.get_full_name())


# UMDStudent class inherits from Student class
class UMDStudent(Student):
    pass
