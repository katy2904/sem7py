def add_log(data):
    with open('phone_book.csv', 'a') as file:
        file.write(data)