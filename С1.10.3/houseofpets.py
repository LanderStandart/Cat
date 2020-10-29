class Client:
    def __init__(self,name='',balance=0):
        self.name = name
        self.balance = balance
    def get_name(self):
        return self.name
    def get_balance(self):
        return (self)
    def show(self):
        print(self.name+' '+str(self.balance))

class List_Clients(Client):
    def __init__(self):
         self.list = []

    def add_client(self,name,balance):
        self.list.append(Client(name,balance))

    def get_list(self):
         for spisok in self.list:
             spisok.show()

class Guest(Client):
    def __init__(self,name='',city='',status=''):
        self.name = name
        self.city = city
        self.status = status

    def show(self):
        print(self.name + ' ' + str(self.city)+ ' ' + str(self.status))

class List_Guests(List_Clients):
    def add_client(self,name,city,status):
        self.list.append(Guest(name,city,status))








