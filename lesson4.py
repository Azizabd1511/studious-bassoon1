# box = ('book','pen')
# for item in box:
#     print
# my_tuple = (6, 4, '2')
# for t in range(1, 100):
#     print(f'{my_tuple}')
# for i in range(1, 101):
#     print(i)
# words = ["adopt", "bake", "beam", "confide", "grill", "wave"]
# past_tense = []
# for word in words:
#     if word[-1] != "e":
#         past_tense.append(word+"ed")
#     else:
#         past_tense.append(word+"d")
#         print(past_tense)
# spam = 'Hello'
# while spam == 'Hello':
#     print(spam)
# Admin_choice = input('Выберите тип: ')
names = []
numbers = []
services = []
while True:
    admin_choice = input('Что хотите сделать? ')

    if admin_choice == 'Имя':
        new_name = input('Введите новое имя ')
        names.append(new_name)
        print(names)
    elif admin_choice == 'Номер':
        new_number = input('Введите новый номер  ')
        names.append(new_number)
        print(numbers)

