def record_data(some_person):
    with open('phonebook.txt', 'a', encoding='utf-8') as f:
        f.write(some_person + '\n')