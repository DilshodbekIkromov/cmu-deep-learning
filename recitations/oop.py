# task 1 
class BankAccount: 
    next_account_number = 1001

    def __init__(self, owner_name, initial_balance=0):
        self.owner_name = owner_name
        self.balance = initial_balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} of money. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Insufficient funds. Current Balance: {self.balance}')
        else:
            self.balance -= amount
            print(f"Withdrew {amount} of money")
    def display_info(self):
        print(f"Account #{self.account_number} | Owner: {self.owner_name} | Balance: {self.balance}")

# acc1 = BankAccount('Dilshodbek', 5000)
# acc2 = BankAccount('Ali', 3000)
# acc1.deposit(2000)
# acc1.withdraw(10000)  # Should show error
# acc1.display_info()
# acc2.display_info()


# task 2 
import bisect
class Student: 
    total_students = 0 
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grade = []
        Student.total_students += 1

    def add_grade(self, grade):
        if grade >= 0 and grade <= 100:
            self.grade.append(grade)
            print(f'Grade of {self.name} is {self.grade[-1]}')
        else:
            print('Give correct grade')
    def get_average(self):
        return sum(self.grade)/len(self.grade)
    @staticmethod
    def grade_to_letter(score):
        breakpoints = [60, 70, 80, 90]
        letters = ['F', 'D', 'C', 'B', 'A']
        return letters[bisect.bisect_right(breakpoints, score)]
    @classmethod
    def get_total_students(cls):
        return cls.total_students



s1 = Student('Dilshodbek', 'S001')
s1.add_grade(95)
s1.add_grade(87)
s1.add_grade(92)
avg = s1.get_average()
print(f'{s1.name}: Average = {avg:.1f}, Letter = {Student.grade_to_letter(avg)}')
print(f'Total students: {Student.get_total_students()}')

    
















