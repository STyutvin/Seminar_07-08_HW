def read_info(searching_info):
    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        flag = False
        for person in info_list:
            if searching_info in person:
                print(person)
                flag = True
        if flag == False:
                print('Контакт не найден.')