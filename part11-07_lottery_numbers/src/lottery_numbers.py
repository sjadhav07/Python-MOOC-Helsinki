# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_num: int, __winning_numbers: list):
        self.week_num = week_num
        self.__winning_numbers = __winning_numbers
    
    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.__winning_numbers])
    
    def hits_in_place(self, numbers: list):
        return [number if number in self.__winning_numbers else -1 for number in numbers]
    