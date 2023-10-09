class CuteCat:
    def __init__(self,cat_name,cat_color,cat_age):
        self.name=cat_name
        self.age=cat_age
        self.color=cat_color

cat1=CuteCat("jojo","橙色",2)

#定义一个学生类
class student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"语文":0,"数学":0,"英语":0}
    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name}(学号：{self.student_id})的成绩为:")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")

li = student("小李","10012")
wang = student("小王","10013")
print(li.name)
print(wang.student_id)
print(li.grades)
li.set_grade("语文",90)
print(li.grades)
li.print_grades()

#继承的使用
#创建一个员工管理系统
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def print_info(self):
        print("员工姓名:"+self.name+" 工号:"+self.id)

class FullTimeEployee(Employee):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary=monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary*self.work_days

zhang = PartTimeEmployee("小张","10026",300,20)
zhang.print_info()
print(zhang.calculate_monthly_pay())