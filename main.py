import datetime
import time

dt = datetime.datetime.today().strftime("%d-%m-%Y")
tc = time.strftime("%H.%M.%S")

print("Local Date: ", tc + " " + dt, "\n")

from application import salary

print("Module salary was imported", "\n")

from application.db import people

print("Module people was imported", "\n")

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
print("Закончено выполнение if __name__ == '__main__'")