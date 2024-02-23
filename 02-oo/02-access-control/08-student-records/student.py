class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = {}

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        if score < 90 and score >= 80:
            return "B" 
        if score <80 and score >= 70:
            return "C"
        if score <70 and score >= 60:
            return "D"
        else:
            return "F"

    def add_course(self, course_name, score):
        letter_grade = self.calculate_letter_grade(score)
        self.__courses[course_name] = letter_grade

    def get_courses(self):
        return self.__courses