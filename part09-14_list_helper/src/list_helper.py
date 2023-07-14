# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        if not my_list:
            return None
        numm = None
        max_count = 0
        for num in set(my_list):
            if my_list.count(num)> max_count:
                max_count = my_list.count(num)
                numm = num
        return numm
    @classmethod
    def doubles(cls, my_list: list):
        lst = []
        for num in set(my_list):
            if my_list.count(num) >= 2:
                lst.append(num)
        return len(lst)
