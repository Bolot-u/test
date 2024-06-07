class Person:
    def __init__(self, fullname, age, is_married):
        self.__fullname = fullname
        self.__age = age
        self.__is_married = is_married

    def get_is_married(self):
        return self.__is_married

    def set_is_married(self, value):
        if isinstance(value, str):
            self.__is_married = value
        else:
            print('Invalid value for is_married')

    def __str__(self):
        return f'My fullname is {self.__fullname} My age is {self.__age}  is married {self.__is_married}'


person1 = Person('Bolot Moldoev', 21, " No")


class Student(Person):
    def __init__(self, fullname, age, is_married):
        super().__init__(fullname, age, is_married)


student1 = Student('Aibek fs', 22, 'No')
student1.set_is_married('s')
print(student1)
print(person1)
