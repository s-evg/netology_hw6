student_rating = {}


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.student_rating = student_rating

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate_for_hw(self, grades):
        k = 0
        for rate in self.grades.values():
            average_rate = sum(rate) / len(rate)
            k += average_rate
        average_hw = round((k / len(self.grades)), 1)
        return average_hw

    def rating(self, name):
        self.student_rating[name] = self.average_rate_for_hw(grades=self.grades)
        return student_rating

    def __str__(self):
        return (
            f'\nИмя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_rate_for_hw(grades=self.grades)}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
            f'Рейтинг студентов: {self.rating(name=self.name)}'
        )


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate_for_lecture(self, grades):
        k = 0
        for rate in self.grades.values():
            average_rate = sum(rate) / len(rate)
            k += average_rate
        average_lecture = round((k / len(self.grades)), 1)
        return average_lecture

    def __str__(self):
        return (
            f'Имя: {self.name}\nФамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.average_rate_for_lecture(grades=self.grades)}'
        )


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_winnie = Student('Винни', 'Пух', 'медведь')
student_winnie.finished_courses += ['Git']
student_winnie.courses_in_progress += ['Python']
student_winnie.courses_in_progress += ['Git', 'HTML']
student_winnie.grades['Git'] = [7, 9]
student_winnie.grades['Python'] = [9, 7]
student_winnie.grades['HTML'] = [10]


student_piglet = Student('Пятачок', 'Поросёнок', 'свинья')
student_piglet.finished_courses += ['Git']
student_piglet.courses_in_progress += ['Python']
student_piglet.courses_in_progress += ['Git', 'HTML', 'CSS']
student_piglet.grades['Git'] = [8, 7]
student_piglet.grades['Python'] = [7, 8]
student_piglet.grades['HTML'] = [8]
student_piglet.grades['CSS'] = [7]


student_robin = Student('Кристофер', 'Робин', 'мальчик')
student_robin.finished_courses += ['Git']
student_robin.courses_in_progress += ['Python']
student_robin.courses_in_progress += ['Git', 'HTML', 'CSS', 'JS']
student_robin.grades['Git'] = [10, 7]
student_robin.grades['Python'] = [9, 8]
student_robin.grades['HTML'] = [10, 8]
student_robin.grades['CSS'] = [9]
student_robin.grades['CSS'] = [8]

# print(student_winnie.finished_courses)
# print(student_winnie.courses_in_progress)
print(student_winnie.grades)
# print(student_winnie.student_list)


lecturer_sava = Lecturer('Сава', 'Филин')
lecturer_sava.courses_attached += ['Git']
lecturer_sava.grades['Git'] = [7, 8, 7, 10, 9, 6, 9, 10]
lecturer_sava.grades['Python'] = [9, 7, 8, 9, 10]

# print(lecturer_sava.name)
# print(lecturer_sava.grades)
# print(lecturer_sava.courses_attached)

student_winnie.rate_lecturer(lecturer_sava, 'Git', 8)

# print(lecturer_sava.grades)

reviewer = Reviewer('Ослик', 'Иа')
# print(reviewer)
# print(lecturer_sava)

# print(student_winnie.name)
# print(lecturer_sava)

print(student_piglet)
print(student_robin)
print(student_winnie)
print(student_robin)
print(student_rating)
