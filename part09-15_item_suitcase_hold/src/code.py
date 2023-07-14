# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    def weight(self):
        return self.__weight
    def name(self):
        return self.__name

class Suitcase:
    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.weigh = 0
        self.itemlist = []
        self.highest_weight = 0
        self.heaviest = Item("", 0)
    
    def add_item(self, item: Item):
        if self.max_weight - self.weigh - item.weight() >=0:
            self.itemlist.append(item)
            a = item.weight()
            self.weigh += a
            if item.weight() > self.highest_weight:
                self.highest_weight = item.weight()
                self.heaviest = item
    def __str__(self):
        if len(self.itemlist) == 1:
            return f"{len(self.itemlist)} item ({self.weigh} kg)"
        return f"{len(self.itemlist)} items ({self.weigh} kg)"
    
    def print_items(self):
        for item in self.itemlist:
            print(f"{item.name()} ({item.weight()} kg)")
    def weight(self):
        return self.weigh
    def heaviest_item(self):
        if len(self.itemlist) == 0:
            return None
        return self.heaviest

class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.lst = []
        self.weight = 0
    
    def add_suitcase(self, suitcase: Suitcase):
        if self.max_weight - self.weight - suitcase.weight() >= 0:
            self.lst.append(suitcase)
            self.weight += suitcase.weight()
    
    def __str__(self):
        if len(self.lst) == 1:
            return f"{len(self.lst)} suitcase, space for {self.max_weight-self.weight} kg"          
        return f"{len(self.lst)} suitcases, space for {self.max_weight-self.weight} kg"

    def print_items(self):
        for suitcase in self.lst:
            for item in suitcase.itemlist:
                print(f"{item.name()} ({item.weight()} kg)")
#OFFICIAL SOLUTION:
# class Item:
#     def __init__(self, name: str, weight: int):
#         self.__name = name
#         self.__weight = weight
 
#     def __str__(self):
#         return f"{self.__name} ({self.__weight} kg)"
 
#     def weight(self):
#         return self.__weight
 
#     def name(self):
#         return self.__name
 
# class Suitcase:
#     def __init__(self, max_weight: int):
#         self.__max_weight = max_weight
#         self.__items = []
 
#     def weight(self):
#         p = 0
#         for item in self.__items:
#             p += item.weight()
#         return p
 
#     def __str__(self):
#         # Use the one-line condition introduced at the end of part 7
#         end_s = "s" if len(self.__items) != 1 else ""
 
#         return f"{len(self.__items)} item{end_s} ({self.weight()} kg)"
 
#     def add_item(self, item):
#         if self.weight() + item.weight() > self.__max_weight:
#             return
 
#         self.__items.append(item)
 
#     def print_items(self):
#         for item in self.__items:
#             print(item)
 
#     def heaviest_item(self):
#         heaviest = self.__items[0]
#         for item in self.__items:
#             if item.weight() > heaviest.weight():
#                 heaviest = item
#         return heaviest
 
# class CargoHold:
#     def __init__(self, max_weight: int):
#         self.__max_weight = max_weight
#         self.__suitcases = []
 
#     def __str__(self):
#         word = "suitcases"
#         if len(self.__suitcases) == 1:
#             word = "suitcase"
 
#         return f"{len(self.__suitcases)} {word}, space for {self.__max_weight-self.weight()} kg"
 
#     def weight(self):
#         p = 0
#         for suitcase in self.__suitcases:
#             p += suitcase.weight()
#         return p
 
#     def add_suitcase(self, suitcase):
#         if self.weight() + suitcase.weight() > self.__max_weight:
#             return
#         self.__suitcases.append(suitcase)
 
#     def print_items(self):
#         for suitcase in self.__suitcases:
#             suitcase.print_items()