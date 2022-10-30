
def view_data(data):
    print(data)


def get_data(text):
    return input(text)


def choice():
    print('Вариант дальнейших действий:\n'
          '   1 - новая запись в справочник\n'
          '   2 - поиск по справочнику\n'
          '   3 - распечатать весь справочник')
    flag = False
    while flag == False:
        select = input()
        try:
            if 1 <= int(select) <= 3:
                return int(select)
            else:
                flag = False
                print('Такого варианта нет, попробуй снова')
        except:
            flag = False
            print('Такого варианта нет, попробуй снова')
    return select

