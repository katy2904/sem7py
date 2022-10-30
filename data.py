import UI

def add_note():
    phone_number = UI.get_data('Введите номер телефона: ')
    name = UI.get_data('Введите имя: ')
    surname = UI.get_data('Введите фамилию: ')
    return phone_number +',' + name + ',' + surname + '\n'


def search(text):
    with open('phone_book.csv', 'r') as file:
        count = 0
        for line in file:
            if text.lower() in line.lower():
                UI.view_data(line.replace(',', ' '))
                count += 1
        if count == 0:
            UI.view_data('Справочник не содержит указанные данные')


def print_list():
    with open('phone_book.csv', 'r') as file:
        for line in file:
            UI.view_data(line.replace(',', ' '))

