class Person:
    def sleep(self):
        print('sleep')
    
class Student(Person):
    def study(self):
        print('Study hard')

class Worker(Person):
    def work(self):
        print('Work hard')

class PartTimer(Student, Worker):
    def find_job(self):
        print('Find a job')

parttime1 = PartTimer()
parttime1.sleep(), parttime1.study(), parttime1.work(), parttime1.find_job()



class Person:
    def __init__(self):
        print('I am a Person')
        
    def sleep(self):
        print('sleep')
    
class Student(Person):
    def __init__(self):
        super().__init__()
        print('I am a student')

    def study(self):
        print('Study hard')

class Worker(Person):
    def __init__(self):
        super().__init__()
        print('I am a worker')

    def work(self):
        print('Work hard')

class PartTimer(Student, Worker):
    def __init__(self):
        super().__init__()
        print('I am a part-timer and student')

    def find_job(self):
        print('Find a job')

# parttime1.sleep(), parttime1.study(), parttime1.work(), parttime1.find_job()
parttime1 = PartTimer()
print(PartTimer.__mro__)