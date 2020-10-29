from houseofpets import List_Clients,Client,Guest,List_Guests

LC = List_Clients()
LC.add_client('Василий Иваныч',100)
LC.add_client('Петька',1000)
# LC.get_list()
command = 'start'

def get_command():
    com = input('С кем работаем '
                '(Гость/Клиент):')
    if com == 'Гость':
        guest()
    else:
        if com =='Клиент':
            client()
        else:
            get_command()

def client():
    com = input('Добавить или Показать:')
    if com == 'Добавить':
        name = input('Имя: ')
        balance = input('Взнос: ')
        LC.add_client(name,balance)
    else:
        if com == 'Показать':
            LC.get_list()
    get_command()

def guest():
    com = input('Добавить или Показать')
    if com == 'Добавить':
        name = input('Имя: ')
        city = input('Город: ')
        status = input('Статус: ')
        LG.add_client(name,city,status)
    else:
        if com == 'Показать':
            LG.get_list()
    get_command()

LG = List_Guests()
LG.add_client('Паша','Москва','Наследник')
LG.get_list()
get_command()
