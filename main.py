
import datetime

from application.db import peaple
from application.salary import calculate_salary

def main():
  d = datetime.date.today()
  print(f'Добрый день, сегодня {d}.')
  global list
  list = list()
  while True:
    q = input('Хотите добавить сотрудника? y/n ')
    if q == 'y':
      add_emp(list)
      calculate_salary(list)
    else:
      break

def add_emp(list):
  emp = peaple.get_employees()
  list.append(emp)
  return list

if __name__ == '__main__':
  main()
