import data
import logger
import UI


def buttom_click():
    choice = UI.choice()
    match choice:
        case 1: logger.add_log(data.add_note())
        case 2: data.search(UI.get_data('Введите текст для поиска: '))
        case 3: data.print_list()
