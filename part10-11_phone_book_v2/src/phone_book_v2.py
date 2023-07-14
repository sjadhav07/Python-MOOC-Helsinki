
# Write your solution here:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers()

    def all_entries(self):
        return self.__persons
    
    def add_address(self, name, addressing):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(addressing)
    
    def get_address(self, name):
        if not name in self.__persons:
            return None
        return self.__persons[name].address()

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_entry(name)
        address = self.__phonebook.get_address(name)
        if numbers == None or numbers == []:
            print("number unknown") 
    
        else:
            for number in numbers:
                print(number) 
    
        if address == None:
            print("address unknown")
            return
        else:
            print(address)
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def execute(self):
        self.help()
        while True:
            
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()
    
class Person:
    def __init__(self, namer : str):
        self.namer = namer
        self.numbers_list = []
        self.addres = None
    
    def name(self):
        return self.namer
    
    def numbers(self):
        return self.numbers_list
    
    def add_number(self, number: str):
        if number not in self.numbers_list:
            self.numbers_list.append(number)
    
    def address(self):
        return self.addres
    
    def add_address(self, addresing: str):
        self.addres = addresing
        



# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
