def calculate_salary(list):
  name = input('Чтобы узнать зар. плату сотрудника введите его имя: ')
  for i in list:
    if i.get('name') == name:
      print(f"Зар. плата {name} - {i.get('salary')}")
    else:
      print('Такого сотрудника нет.')
