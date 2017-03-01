#! /usr/bin/env python3
# coding = utf-8

# school_member_adt.py - 类定义实例：学校人事管理系统中的类

import datetime


class PersonTypeError(TypeError):
    pass


class PersonValueError(ValueError):
    pass


class Person:
    "公共人员类"
    _num = 0

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and sex in ("女", "男")):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError("Wrong date:", birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self): return self._id

    def name(self): return self._name

    def sex(self): return self._sex

    def birthday(self): return self._birthday

    def age(self):
        return (datetime.date.today().year - self._birthday.year)

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name = name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another._id

    @classmethod
    def num(cls): return cls._num

    def __str__(self):
        return " ".join((self._id, self._name, self._sex, str(self._birthday)))

    def details(self):
        return ", ".join((
            "编号: " + self._id,
            "姓名: " + self._name,
            "性别: " + self._sex,
            "出生日期: " + str(self._birthday)
        ))


class Student(Person):
    "学生类"
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        super().__init__(name, sex, birthday, Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError("No this score selected:", course_name)
        self._courses[course_name] = score

    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    def details(self):
        return ", ".join((
            super().details(),
            "入学日期: " + str(self._enroll_date),
            "院系: " + self._department,
            "课程记录: " + str(self.scores())
        ))


class Staff(Person):
    "教职工类"
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday)
        return "0{:04}{:05}".format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday, Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError("Wrong date:", entry_date)
        else:
            self._entry_date = datetime.date.today()
        self._salary = 1720
        self._department = "未定"
        self._position = "未定"

    def set_salary(self, amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount

    def set_position(self, position):
        self._position = position

    def set_department(self, department):
        self._department = department

    def details(self):
        return ", ".join((
            super().details(),
            "入职日期: %s" % (self._entry_date),
            "院系: " + self._department,
            "职位: " + self._position,
            "工资: %s" % (self._salary)
        ))

if __name__ == '__main__':
    print("Test for Person:")
    p1 = Person("谢雨洁", "女", (1995, 7, 30), "1201510111")
    p2 = Person("汪力强", "男", (1990, 2, 17), "1201380324")
    plist = [p1, p2]
    print("Person num:%s" % (Person.num()))
    for p in plist:
        print(p)
    print("After sorting:")
    plist.sort()
    for p in plist:
        print(p.details())
    print("\nTest for Student:")
    s1 = Student("池永祥", "男", (1987, 8, 2), "软件学院")
    s2 = Student("杨永祥", "女", (1987, 8, 2), "软件学院")
    s1.set_course("compute")
    s1.set_score("compute", 80)
    slist = [s1, s2]
    for s in slist:
        print(s.details())
    print("Person num:%s" % (Person.num()))
    print("\nTest for Staff:")
    st1 = Staff("张子玉", "女", (1974, 10, 16))
    st2 = Staff("李国栋", "男", (1962, 2, 16))
    stlist = [st1, st2]
    for st in stlist:
        print(st.details())
    st1.set_department("数学")
    st1.set_position("副教授")
    st1.set_salary(8400)
    for st in stlist:
        print(st.details())
